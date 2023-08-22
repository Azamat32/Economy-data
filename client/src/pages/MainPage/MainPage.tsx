import EconomyItem from "../../widgets/EconomyItem/EconomyItem";
import "./MainPage.scss"
type Props = {};

const MainPage = (_props: Props) => {
  const array = [{ title: "test1", link: "test1" }];
  const items = array.map((item) => {
    return <EconomyItem title={item.title} link={item.link} />;
  });
  return (
    <div className="main">
      <div className="container">
        <div className="main_inner">
        {items}

        </div>
      </div>
    </div>
  );
};

export default MainPage;
