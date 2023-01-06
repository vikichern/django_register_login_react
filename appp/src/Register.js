import React, { useState } from "react";
import axios from "axios";

const Register = () => {
  const SERVER = "http://127.0.0.1:8000/register/";

  const [username, setuName] = useState("");
  const [password, setpwd] = useState("");
  const [regStatus, setregStatus] = useState("");

  const do_register = async () => {
    const res = await axios.post(SERVER, { username, password });
    setregStatus(res.data);
  };

  return (
    <div>
      <h1>Register</h1>
      Uname:
      <input onChange={(e) => setuName(e.target.value)} />
      pwd:
      <input onChange={(e) => setpwd(e.target.value)} />
      <button onClick={() => do_register()}>Register/signup</button>
      {regStatus === "error" ? (
        <h1 style={{ color: "red" }}>{regStatus}</h1>
      ) : (
        <h1>{regStatus}</h1>
      )}
    </div>
  );
};
// 1 === "1" false
// 1 =="1" true
export default Register;
