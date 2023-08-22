import "./EconomyItem.scss"

type EconomyItem = {
    link:string
    title: string
}
const EconomyItem = (props: EconomyItem) => {
    const {title , link} = props
  return (
    <a href={link}>
        {title}
    </a>
  )
}

export default EconomyItem