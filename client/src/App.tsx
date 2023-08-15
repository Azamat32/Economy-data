import { useState, useEffect } from 'react'

import './App.css'
import Navbar from './widgets/Navbar/Navbar';
function App() {
  const [data, setData] = useState([])
  console.log(data);
  
  useEffect(() => {
   
  }, [])

  return (
    <>
     <Navbar />
    </>
  )
}

export default App
