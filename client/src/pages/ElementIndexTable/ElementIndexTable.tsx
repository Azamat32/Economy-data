import { useParams } from "react-router-dom";
import axios from "axios";
import { useQuery } from "react-query";
import "./ElementIndexTable.scss";
type RouteParams = {
  id: string; // Define the route parameter as a string
};
type Props = {};

const apiEndpoint = "http://127.0.0.1:8000/api/economic_index"; // Replace with your API endpoint

const fetchElementById = async (id: any) => {
  const response = await axios.post(apiEndpoint, { id });
  return response.data;
};

const ElementIndexTable = (_props: Props) => {
  const { id } = useParams<RouteParams>();

  const { data, isLoading } = useQuery(["getElementById", id], () =>
    fetchElementById(id)
  );

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
      </div>
    </div>
  );
};

export default ElementIndexTable;
