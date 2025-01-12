import React, { useContext } from "react";
import Header from "../templates/Header";
import { Navigate, useLocation } from "react-router-dom";
import { useState } from "react";
import { LoginUserContext } from "../providers/LoginUserProvider";
import ReadCsv from "../elements/ReadCsv";
import BarChart from "../elements/BarChart";
import SelectYear from "../elements/SelectYear";
import ReadDatabase from "../elements/ReadDatabase";

const Home = () => {
  const { isLogined } = useContext(LoginUserContext);
  const [data, setData] = useState([]);
  const handleDataChange = (newData) => {
    setData(newData);
  };
  const [year, setYear] = useState("");
  const handleYearChange = (newYear) => {
    setYear(newYear);
  };
  if (!isLogined) {
    return <Navigate to="/login" />;
  } else {
    return (
      <>
        <Header />
        <h3>CSVをデータベースへ格納</h3>
        <ReadCsv handleDataChange={handleDataChange} />
        <SelectYear handleYearChange={handleYearChange} />
        <ReadDatabase year={year} handleDataChange={handleDataChange} />
        <h3>グラフ表示</h3>
        <BarChart data={data} />
      </>
    );
  }
};

export default Home;
