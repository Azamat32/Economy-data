import { useParams } from "react-router-dom";
import {useEffect , useState} from "react"
import axios from "axios";
import { useQuery } from "react-query";
import "./ElementIndexTable.scss";
import * as  XLSX from "xlsx"; // Import the xlsx library

type RouteParams = {
  id: string; // Define the route parameter as a string
};
type Props = {};

const apiEndpoint = "http://127.0.0.1:8000/api/economic_index"; // Replace with your API endpoint
const fetchElementById = async (id: any) => {
  console.log(id);
  
  const response = await axios.post(apiEndpoint, { id });
  return response.data;
};


const fetchExcelFile = async () => {
  const response = await axios.get(`${apiEndpoint}/excel`, {
    responseType: "blob", // Set the response type to blob
  });
  return response.data;
};



const ElementIndexTable = (_props: Props) => {
  const { id } = useParams<RouteParams>();

  const { data, isLoading } = useQuery(["getElementById", id], () =>
    fetchElementById(id)
  );

  const [excelData, setExcelData] = useState<Blob | null>(null); // Provide null as the initial state
  const [sheetData, setSheetData] = useState<any[][] | null>(null); // State to store the Excel sheet data

  useEffect(() => {
    fetchExcelFile()
      .then((excelFile) => {
        // Create a blob URL for the Excel file
        const blob = new Blob([excelFile], {
          type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        });
  
        setExcelData(blob);
  
        // Parse the Excel file
        parseExcelFile(blob);
      })
      .catch((error) => {
        console.error("Error fetching Excel file:", error);
      });
  }, [id]);
  

  const parseExcelFile = (file: Blob) => {
    const reader = new FileReader();
  
    reader.onload = (e) => {
      const data = (e.target as FileReader).result;

      const workbook = XLSX.read(data, { type: "binary" });

      
      // Assuming you want the data from the first sheet
      const sheetName = workbook.SheetNames[0];
      const sheet = workbook.Sheets[sheetName];
  
      // Parse the sheet data into an array of objects
      const excelData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
  
      // Set the parsed data in state
      setSheetData(excelData as any[][]);

    };
  
    reader.readAsBinaryString(file);
  };
  




  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (!data) {
    return <div>No data found.</div>;
  }
  return (
    <div>
      <div className="table_title">
        <h2> {data.name}</h2>
        {/* {excelData && (
          <a href={excelData} download="test.xlsx">
            Download Excel File
          </a>
        )} */}

{sheetData && (
      <div>
        <h3>Excel Data</h3>
        <table>
          <thead>
            <tr>
              {sheetData[0].map((header: string, index: number) => (
                <th key={index}>{header}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {sheetData.slice(1).map((row: any[], rowIndex: number) => (
              <tr key={rowIndex}>
                {row.map((cell: any, cellIndex: number) => (
                  <td key={cellIndex}>{cell}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    )}
      </div>
    </div>
  );
};

export default ElementIndexTable;
