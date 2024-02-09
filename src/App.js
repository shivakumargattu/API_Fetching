
import './App.css';
import {useState,useEffect} from "react"

function App() {
  
  const [data, setData]=useState([])
  
  useEffect(()=>{
     
     fetch("https://jsonplaceholder.typicode.com/todos")
     .then((res)=>res.json())
     .then((userData)=>setData(userData))
     

  },[])
  
  console.log(data)
  return (
    <div className="App">
     <h1>Fetching Data</h1>
     <div >
     <div className='bgContainer'>
     {data.map((task)=>{

      return(
        
         <div key={task.id} style={{padding:"10px",width:"200px", backgroundColor:"#fff", margin:"10px"}}  >
          <h4>{task.title}</h4>
          <button style={{  backgroundColor:task.completed?"green":"red", color:"#fff",padding:"10px",borderRadius:"8px",borderWidth:"0px"}  }>{task.completed?"Completed":"In-Completd"}</button>

          </div>
       
      )
     })}
    </div>
    </div>
    </div>
  );
}

export default App;
