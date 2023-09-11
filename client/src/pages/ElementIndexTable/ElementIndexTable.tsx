import { useParams } from "react-router-dom";
import {useEffect , useState} from "react"
import axios from "axios";
import { useQuery } from "react-query";
import "./ElementIndexTable.scss";
import ReactExcelRender from "../../widgets/ReactExcelRenderer/ReactExcelRender";
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

  const [excelData, setExcelData] = useState<string | null>(null); // Provide null as the initial state
  const [sheetData, setSheetData] = useState<any[][] | null>(null); // State to store the Excel sheet data

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
        {excelData && (
          <a href={excelData} download="test.xlsx">
            Download Excel File
          </a>
        )}
      </div>
    </div>
  );
};

export default ElementIndexTable;
