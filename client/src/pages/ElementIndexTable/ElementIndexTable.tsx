import { useEffect, useState } from "react";
import axios from "axios";
import * as XLSX from "xlsx";
import "./ElementIndexTable.scss";
import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import Loader from "../../widgets/Loader/Loader";
const apiEndpoint = "http://127.0.0.1:8000/api";
type RouteParams = {
  id: string; // Define the route parameter as a string
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
  const [editableData, setEditableData] = useState<any[][] | null>(null);
  const [isEditing, setIsEditing] = useState(false);
  const [tableId, setTableId] = useState<number>(1);
  const { data, isLoading } = useQuery(["getElementById", id], () =>
    fetchElementData(id)
  );

  useEffect(() => {
    console.log(data);

    if (data && data.tables && data.tables.length > 0) {
      // Map each table object to a promise that fetches the Excel file

      const fetchPromises = data.tables.map((table: { id: number }) => {
        setTableId(table.id);
        return fetchExcelFile(table.id);
      });

      // Use Promise.all to send multiple requests concurrently
      Promise.all(fetchPromises)
        .then((excelBlobs) => {
          // Combine the fetched Excel blobs into a single blob (if needed)
          // For example, if you want to merge them into one Excel file
          const combinedBlob = combineExcelBlobs(excelBlobs);

          // Set the combined blob and parse it
          setExcelData(combinedBlob);
          parseExcelFile(combinedBlob);
        })
        .catch((error) => {
          console.error("Error fetching Excel files:", error);
        });
    }
  }, [data]);

  const fetchExcelFile = async (tableId: number) => {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/economic_index_excel/${tableId}`,
      {
        responseType: "blob",
      }
    );

    return response.data;
  };

  // Utility function to combine multiple Excel blobs (if needed)
  const combineExcelBlobs = (blobs: any[]) => {
    // Example: Just return the first blob (you can customize this logic)
    return blobs[0];
  };

  const parseExcelFile = (file: Blob) => {
    const reader = new FileReader();

    reader.onload = (e) => {
      const data = (e.target as FileReader).result as string;
      const workbook = XLSX.read(data, { type: "binary" });

      // Assuming you want the data from the first sheet
      const sheetName = workbook.SheetNames[0];
      const sheet = workbook.Sheets[sheetName];

      // Parse the sheet data into an array of objects
      const excelData = XLSX.utils.sheet_to_json(sheet, {
        blankrows: false,
        defval: "",
        header: 1,
      });

      // Set the parsed data in state
      setSheetData(excelData as any[][]);
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
    // Создайте копию текущего состояния sheetData
    const updatedData = [...(sheetData || [])];

    // Обновите значение ячейки в копии данных
    updatedData[rowIndex + 1][cellIndex] = newValue;

    // Обновите состояние sheetData
    setSheetData(updatedData);
  };

  const saveExcelData = () => {
    if (!sheetData) {
      console.error("Data is missing or incomplete.");
      return;
    }

    // Create a new Excel workbook
    const wb = XLSX.utils.book_new();

    // Create a new worksheet
    const ws = XLSX.utils.aoa_to_sheet(sheetData);

    // Add the worksheet to the workbook
    XLSX.utils.book_append_sheet(wb, ws, "Sheet1");

    // Convert the workbook to an Excel file content as a string
    const excelFileContent = XLSX.write(wb, {
      bookType: "xlsx",
      type: "binary",
    });

    // Convert the Excel file content to a Blob
    const blob = new Blob([s2ab(excelFileContent)], {
      type: "application/octet-stream",
    });

    // Create a FormData object to send the blob
    const formData = new FormData();
    formData.append("excel_file", blob, "test.xlsx");

    // Send a POST request to your Django endpoint
    axios
      .post(`http://127.0.0.1:8000/api/save_excel/${tableId}/`, formData)
      .then((response) => {
        console.log("Excel data saved successfully:", response.data);
      })
      .catch((error) => {
        console.error("Error saving Excel data:", error);
      });
    setIsEditing(!isEditing);
  };

  // Utility function to convert a string to an ArrayBuffer
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
      {isLoading && <div>Loading...</div>}
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
        <div>No data found.</div>
      )}
      {excelData && (
        <div className="links">
          <a href={window.URL.createObjectURL(excelData)} download={`${data.name}.xlsx`}>
            Download Excel File
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
