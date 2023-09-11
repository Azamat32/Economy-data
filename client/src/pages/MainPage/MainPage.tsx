import { useEffect, useState } from "react";
import axios from "axios";
import "./MainPage.scss";
import close from "../../assets/Gallery/close.svg"
type Props = {};
type TableTitles = {
  id: number;
  name: string;
};

const api = "economic_indices"
const MainPage = (_props: Props) => {
  const [isOpened , setIsOpened] = useState(false)
  const [tablesTitle, setTablesTitle] = useState<TableTitles[]>([]);
  const [dropdownContent, setDropdownContent] = useState<{
    id: number;
    name: string;
    path: string | null;
    macro_topic: number;
  }[]>([]);
  useEffect(() => {
    fetchData();
  }, []);
  const handleModal = (isOpened:boolean) => {
    console.log(isOpened);

      setIsOpened(!isOpened) 
  }
  const handleClick = async (id: number) => {
    console.log(id)
    try {
      const response = await axios.post(
        `http://127.0.0.1:8000/api/${api}`,
        
        
        { id } // Sending the id in the request payload
      );
      setDropdownContent(response.data); // Assuming the response data should be saved
      
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
  useEffect(() => {
    console.log(dropdownContent); // Log dropdownContent whenever it changes
  }, [dropdownContent]);
  let tables = tablesTitle.map((item) => {
    return (
      <div className="title-wrapper" key={item.id}>
      <div
        onClick={() => handleClick(item.id)}
        className="title"
      >
        {item.name}
        <div
        onClick={() => handleModal(isOpened)}
        className="open-modal-button"
      >
      </div>
      </div>
    
    </div>
    );
  });
  return (
    <div className="main">
      <div className="container">
      <div className={`Modal ${isOpened ? 'active' : ''}`}>     
          <div className="modal_inner">
              <img className="close" src={close} onClick={() => handleModal(isOpened)} />
              <div className="modal_list">
              {dropdownContent.map((item) => (
          <a key={item.id} href={item.id.toString()} className="list-item">
        {item.name}
          </a>
        ))}
              </div>
        </div>
    </div>
        <div className="main_inner">{tables}</div>

      </div>
    </div>
  );
};

export default MainPage;
