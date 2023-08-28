import { useEffect, useState } from "react";
import EconomyItem from "../../widgets/EconomyItem/EconomyItem";
import axios from "axios";
import "./MainPage.scss";
type Props = {};
type TableTitles = {
  id: number;
  name: string;
};
const api = "economic_indices"
const MainPage = (_props: Props) => {
  const [tablesTitle, setTablesTitle] = useState<TableTitles[]>([]);
  const [tableItem , setTableItem] = useState()
  useEffect(() => {
    fetchData();
  }, []);
  const handleClick = async (id: number) => {
    try {
      const response = await axios.post(
        `http://127.0.0.1:8000/api/${api}`,
        { id } // Sending the id in the request payload
      );
      setTableItem(response.data); // Assuming the response data should be saved
      console.log(tableItem);
      
    } catch (error) {
      console.log("Error:", error);
    }
  };

  const fetchData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/topics");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setTablesTitle(data);
      
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };
  let tables = tablesTitle.map((item) => {
    return (
        <div onClick={() => handleClick(item.id)} className="title" key={item.id}>{item.name} </div>
    );
  });
  return (
    <div className="main">
      <div className="container">
        <div className="main_inner">{tables}</div>
      </div>
    </div>
  );
};

export default MainPage;
