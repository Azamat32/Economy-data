import "./NotFound.scss";

type Props = {}

const NotFound = (_props: Props) => {
  return (  
    <div className="container">
      <h1>404</h1>
      <p>Sorry, the page you are looking for could not be found.</p>
      <a className="notFoundLink" href="/">Back</a>
    </div>
  
  )
}

export default NotFound
