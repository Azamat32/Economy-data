import axios from 'axios';
import  { useEffect, useState } from 'react';
import * as XLSX from 'xlsx';
type Props = {}

const apiEndpoint = "http://127.0.0.1:8000/api/economic_index"; // Replace with your API endpoint

const fetchExcelFile = async () => {
    const response = await axios.get(`${apiEndpoint}/excel`, {
      responseType: "blob", // Set the response type to blob
    });
    return response.data;
  };

const ReactExcelRender = (_props: Props) => {
    const [data, setData] = useState<any[][] | null>(null);
  const [excelData, setExcelData] = useState<string | null>(null); // Provide null as the initial state

    useEffect(() => {
        // Fetch the Excel file when the component mounts
        fetchExcelFile()
          .then((excelFile) => {
            // Create a blob URL for the Excel file
            const blob = new Blob([excelFile], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const url = window.URL.createObjectURL(blob);
            setExcelData(url);
          })
          .catch((error) => {
            console.error("Error fetching Excel file:", error);
          });
      }, [id]);
    useEffect(() => {
      // Replace with the actual path to your Excel file
        
      // Fetch the Excel file
      fetch(excelData)
        .then((response) => response.arrayBuffer())
        .then((arrayBuffer) => {
          // Parse the Excel file data
          const workbook = XLSX.read(arrayBuffer, { type: 'array' });
  
          // Assuming there's only one sheet in the Excel file
          const sheet = workbook.Sheets[workbook.SheetNames[0]];
  
          // Convert the sheet data to an array of arrays
          const sheetData: any[][] = XLSX.utils.sheet_to_json(sheet, { header: 1 });
  
          setData(sheetData);
        })
        .catch((error) => {
          console.error(error);
        });
    }, []);
  
    if (!data) {
      return <div>Loading Excel file...</div>;
    }
  
    return (
      <div>
        {/* Render your Excel data here */}
        {data.map((row, rowIndex) => (
          <div key={rowIndex}>
            {row.map((cell, colIndex) => (
              <span key={colIndex}>{cell}</span>
            ))}
          </div>
        ))}
      </div>
    );
  };


export default ReactExcelRender