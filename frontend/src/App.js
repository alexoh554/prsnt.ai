import { useState, useEffect } from 'react'
import axios from "axios";
import './App.css';

function App() {
   // new line start
   const [data, setData] = useState(null)

   useEffect( () => {
    axios.get("http://127.0.0.1:5000/")
    .then((response) => {
       const res =response.data
       setData(({
         title: res.title}))
     }).catch((error) => {
       if (error.response) {
         console.log(error.response)
         console.log(error.response.status)
         console.log(error.response.headers)
         }
     })}
   )


    return (
    <>
      <div className="App">
        {data ? (
          <h1>{data.title}</h1>
        ) : (
          <p>Loading...</p>
        )}
      </div>
    </>
  );
    
}

export default App;
