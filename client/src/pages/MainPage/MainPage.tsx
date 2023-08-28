import { useEffect, useState } from "react";
import EconomyItem from "../../widgets/EconomyItem/EconomyItem";
import "./MainPage.scss";
type Props = {};
type Item = {
  macro: {
    id: number;
    name: string;
  };
  name: string;
  link: string;
};

const MainPage = (_props: Props) => {
  const [items, setItems] = useState<Item[]>([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setItems(data); // Assuming the API returns an array of items
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };
  console.log(items);
  let tables = items.map((item) => {
    return (
      <>
        <div className="title">{item.macro.name} : </div>
        <div className="text">{item.name}</div>
      </>
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
