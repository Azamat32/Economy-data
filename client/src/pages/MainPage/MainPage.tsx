import { Key, useEffect, useState } from "react";
import axios from "axios";
import "./MainPage.scss";

import { useQuery, useQueryClient } from "react-query";
import Loader from "../../widgets/Loader/Loader";
import { NavLink } from "react-router-dom";

type Props = {};
type TableTitles = {
  id: number;
  name: string;
};

const MainPage = (_props: Props) => {
  const [tablesTitle, setTablesTitle] = useState<TableTitles[]>([]);
  const [selectedId, setSelectedId] = useState<number>(
    1
  );
    
  useEffect(() => {
    
    fetchData();
  }, []);

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

  const queryClient = useQueryClient();

  const fetchTables = async (id: number) => {

    const response = await axios.post(
      `http://127.0.0.1:8000/api/economic_indices`,
      {
        id,
      }
    );
    return response.data;
  };

  const {
    isLoading,
    data: fetchedTables,
  } = useQuery(
    ["fetchTables", selectedId],

    () => fetchTables(selectedId),
    {
      enabled: true, // Initially, query is disabled

      onError: (error) => {
        console.error("Error:", error);
      },
    }
  );

  const handleClick = async (id: number) => {
    setSelectedId(id);

    await queryClient.invalidateQueries(["fetchTables", id]);
  };

  let tables = tablesTitle.map((item) => {
    return (
      <div className="title-wrapper" key={item.id}>
        <div onClick={() => handleClick(item.id)} className="title">
          {item.name}
        </div>
      </div>
    );
  });
  return (
    <div className="main">
      <div className="container">
        <div className="main_inner">
          <div className="table_titles">{tables}</div>
          <div className="table_links">
            {isLoading ? ( // Use isLoading to conditionally render the loader
              <Loader />
            ) : (
              fetchedTables &&
              fetchedTables.map((item: { id: Key; name: string }) => (
                <NavLink
                  key={item.id}
                  to={`/economic_index/${item.id}`}
                  className="list-item"
                >
                  {item.name}
                </NavLink>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default MainPage;
