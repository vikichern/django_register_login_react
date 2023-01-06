import React, { useEffect, useState } from "react";
import axios from "axios";
import Register from "./Register";

const App = () => {
  const SERVER = "http://127.0.0.1:8000/";
  const [tasks, settasks] = useState([]);
  const [uName, setuName] = useState("");
  const [pwd, setpwd] = useState("");
  const [access, setaccess] = useState("");
  const [refresh, setrefresh] = useState("");
  const [logged, setlogged] = useState(false);
  const getTasks = async () => {
    const config = {
      headers: {
        Authorization: `Bearer ${access}`,
      },
    };
    await axios
      .get(SERVER + "tasks/", config)
      .then((res) => settasks(res.data));
  };

  useEffect(() => {
    if (access) {
      setlogged(true);
      getTasks();
    }
  }, [access]);

  const login = async () => {
    const data = {
      username: uName,
      password: pwd,
    };
    const res = await axios.post(SERVER + "login/", data);
    setaccess(res.data.access);
    setrefresh(res.data.refresh);
  };

  return (
    <div>
      <Register></Register>
      <h1>Login</h1>
      Uname:
      <input onChange={(e) => setuName(e.target.value)} />
      pwd:
      <input onChange={(e) => setpwd(e.target.value)} />
      <button onClick={() => login()}>Login/signin</button>
      <hr></hr>
      <button onClick={() => getTasks()}>get Tasks</button>
      <hr></hr>
      {logged ? "welcome mr/mrs: " + uName : "you need 2 login"}
      <hr></hr>
      {/* condition && True */}
      {tasks.length > 0 && <h1>Your data</h1>}
      {/*condition ? True : False  */}
      {tasks.length === 0
        ? "no data - please login"
        : tasks.map((task, i) => (
            <div key={i}>
              Title: {task.title},desc: {task.description}
            </div>
          ))}
    </div>
  );
};

export default App;
