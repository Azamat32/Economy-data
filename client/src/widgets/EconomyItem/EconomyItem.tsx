import "./EconomyItem.scss";

type EconomyItem = {
  title: string;
  list: {
    id: number;
    name: string;
    path: string | null;
    macro_topic: number;
  }[];
};
const EconomyItem = (props: EconomyItem) => {
  const { title,list  } = props;
  return <div className="EconomyItem" >
    <div className="economy_item_title">
    {title}
    </div>
    <div className="economy_item_list">
    {list.map((item) => (
          <a key={item.id} href={item.id.toString()} className="list-item">
            {/* Render the properties of each item */}
            <span>Name: {item.name}</span>
          </a>
        ))}
    </div>
   </div>;
};

export default EconomyItem;
