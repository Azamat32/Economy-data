import  { useEffect, useState } from "react";
import axios from "axios";
import * as XLSX from "xlsx";
import "./ElementIndexTable.scss"
import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
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

  const [isLoadingTable, setIsLoadingTable] = useState(false);

  
  const { data, isLoading } = useQuery(["getElementById", id], () =>
  fetchElementData(id)

  );

  useEffect(() => {
    console.log(data);
    
    if (data && data.tables && data.tables.length > 0) {
      // Assuming you want the first table path
      const tablePath = data.tables[0].path;
      fetchExcelFile(tablePath);
    }
  }, [data]);

  const fetchExcelFile = async (tablePath: string) => {
    const response = await axios.get(`http://127.0.0.1:8000/static/tables/${tablePath}.xlsx`, {
      responseType: "blob",
    });

    const blob = new Blob([response.data], {
      type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    });
    setExcelData(blob);
    parseExcelFile(blob);
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
        blankrows:false,
        defval: '' ,
        header: 1,
      });

      // Set the parsed data in state
      setSheetData(excelData as any[][]);
      
    };

    reader.readAsBinaryString(file);
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }// ...
  if (sheetData){
    console.log(sheetData);
  }

return (
  <div className="container">
    <div className="table-title">
      <h2>Excel Data</h2>
      <h2> {data.name}</h2>
    </div>
    {isLoading && <div>Loading...</div>}
    {sheetData && sheetData[0] ? (
      <div className="table">
        <div className="table_head">
          <div>
            {sheetData[0].map((header: string, index: number) => (
              
              <p key={index}>{header}</p>
            ))}
          </div>
        </div>
        <div className="table_body">
          {sheetData.slice(1).map((row: any[], rowIndex: number) => (
            <div key={rowIndex}>
              {row.map((cell: any, cellIndex: number) => (
                 
                <p key={cellIndex}>{cell} <span className="border_elemnt"></span></p>    
           
               
              ))}
            </div>
          ))}
        </div>
      </div>
    ) : (
      <div>No data found.</div>
    )}
    {excelData && (
      <div className="download-link">
        <a href={window.URL.createObjectURL(excelData)} download="test.xlsx">
          Download Excel File
        </a>
      </div>
    )}
  </div>
);}


export default ElementIndexTable;
