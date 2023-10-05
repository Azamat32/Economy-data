import { SetStateAction, useEffect, useState } from "react";
import axios from "axios";
import * as XLSX from "xlsx";
import "./ElementIndexTable.scss";
import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import Loader from "../../widgets/Loader/Loader";


const apiEndpoint = "http://127.0.0.1:8000/api";
const excelDownloadUrl = "http://127.0.0.1:8000/api/save_excel";


type RouteParams = {
  id: string;
};
const fetchElementData = async (id: any) => {
  const response = await axios.get(`${apiEndpoint}/economic_index/${id}`);
  const data = response.data;
  return data;
};

const ElementIndexTable = () => {
  const { id } = useParams<RouteParams>();

  const [excelData, setExcelData] = useState<Blob | null>(null);
  const [sheetData, setSheetData] = useState<any[][] | null>(null);
  const [excelList, setExcelList] = useState<any[] | null>(null);

  const [isEditing, setIsEditing] = useState(false);
  const [tableId, setTableId] = useState<any[] | null>(null);
  const { data, isLoading } = useQuery(["getElementById", id], () =>
    fetchElementData(id)
  );
  useEffect(() => {
    console.log(excelList);
    console.log(tableId);
    
  }, [excelList]);
  useEffect(() => {
    console.log(data);
    
    if (data && data.tables && data.tables.length > 0) {
      const newTableIds: SetStateAction<any[] | null> = [];
      const fetchPromises = data.tables.map((table: { id: number }) => {
        newTableIds.push(table.id);
       
        
        return fetchExcelFile(table.id);
      });

      Promise.all(fetchPromises)
        .then((excelBlobs) => {
       
          const combinedBlob = combineExcelBlobs(excelBlobs);

          setExcelData(combinedBlob);
          parseExcelFile(combinedBlob);
          setTableId(newTableIds);
        console.log(excelList);
        })
        .catch((error) => {
          console.error("Error fetching Excel files:", error);
        });
    }
  }, [data]);

  const fetchExcelFile = async (tableId: number) => {
    const response = await axios.get(
      `${apiEndpoint}/economic_index_excel/${tableId}`,
      {
        responseType: "blob",
      }
    );

    return response.data;
  };

  const combineExcelBlobs = (blobs: any[]) => {
    
    return blobs[0];
  };

  const parseExcelFile = (file: Blob) => {
    const reader = new FileReader();

    reader.onload = (e) => {
      const data = (e.target as FileReader).result as string;
      const workbook = XLSX.read(data, { type: "binary" });

      const sheetName = workbook.SheetNames[0];
      const sheet = workbook.Sheets[sheetName];

      const excelData = XLSX.utils.sheet_to_json(sheet, {
        blankrows: false,
        defval: "",
        header: 1,
      });
      setSheetData(() => {
        const updatedSheetData = excelData as any[][];
        return updatedSheetData;
      });
  
      setExcelList((prevExcelList) => [...(prevExcelList || []), excelData]);
  
    };

    reader.readAsBinaryString(file);
  };

  if (isLoading) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

  const handleCellEdit = (
    newValue: string,
    rowIndex: number,
    cellIndex: number
  ) => {
    const updatedData = [...(sheetData || [])];

    updatedData[rowIndex + 1][cellIndex] = newValue;

    setSheetData(updatedData);
  };

  const saveExcelData = () => {
    if (!sheetData) {
      console.error("Data is missing or incomplete.");
      return;
    }

    const wb = XLSX.utils.book_new();

    const ws = XLSX.utils.aoa_to_sheet(sheetData);

    XLSX.utils.book_append_sheet(wb, ws, "Sheet1");

    const excelFileContent = XLSX.write(wb, {
      bookType: "xlsx",
      type: "binary",
    });

    const blob = new Blob([s2ab(excelFileContent)], {
      type: "application/octet-stream",
    });

    const formData = new FormData();
    formData.append("excel_file", blob, "test.xlsx");
    
    axios
      .post(`${excelDownloadUrl}/${tableId?.[0]}/`, formData)
      .then((response) => {
        console.log("Excel data saved successfully:", response.data);
      })
      .catch((error) => {
        console.error("Error saving Excel data:", error);
      });
    setIsEditing(!isEditing);
  };

  const s2ab = (s: string) => {
    const buf = new ArrayBuffer(s.length);
    const view = new Uint8Array(buf);
    for (let i = 0; i < s.length; i++) {
      view[i] = s.charCodeAt(i) & 0xff;
    }
    return buf;
  };
  return (
    <div className="container">
      <div className="table-title">
        <h2> {data.name}</h2>
      </div>
      {isLoading && <div>Загрузка</div>}
      {sheetData && sheetData[0] ? (
        <div className="table_container">
          <div className="table">
            <div className="table_head">
              <div className="table_row">
                {sheetData[0].map((header: string, index: number) => (
                  <div className="table_body_element" key={index}>
                    {header}
                  </div>
                ))}
              </div>
            </div>
            <div className="table_body">
              {sheetData.slice(1).map((row: any[], rowIndex: number) => (
                <div className="table_row" key={rowIndex}>
                  {row.map((cell: any, cellIndex: number) => (
                    <div className="table_body_element" key={cellIndex}>
                      {isEditing ? (
                        <input
                          type="text"
                          value={cell}
                          onChange={(e) =>
                            handleCellEdit(e.target.value, rowIndex, cellIndex)
                          }
                        />
                      ) : (
                        cell
                      )}
                    </div>
                  ))}
                </div>
              ))}
            </div>
          </div>
        </div>
      ) : (
        <div>Сервер не смогл загрузить таблицу</div>
      )}
      {excelData && (
        <div className="links">
          <a
            href={window.URL.createObjectURL(excelData)}
            download={`${data.name + tableId}.xlsx`}
          >
            Загрузить экзель файл
          </a>

          {isEditing ? (
            <button onClick={saveExcelData}>Сохранить изменения</button>
          ) : (
            <button onClick={() => setIsEditing(!isEditing)}>
              Добавить новые данные
            </button>
          )}
        </div>
      )}
    </div>
  );
};

export default ElementIndexTable;
