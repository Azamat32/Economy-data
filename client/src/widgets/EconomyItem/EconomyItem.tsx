import "./EconomyItem.scss";

type EconomyItem = {
  link: string;
  title: string;
};
const EconomyItem = (props: EconomyItem) => {
  const { title, link } = props;
  return <a className="EconomyItem" href={link}>{title}</a>;
};

export default EconomyItem;
