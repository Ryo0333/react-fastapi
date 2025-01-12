import React, { useEffect } from "react";
import { useReadSales } from "../hooks/useReadSales";

const ReadDatabase = (props) => {
  const { year, handleDataChange } = props;
  const { onClickReadSales } = useReadSales();
  useEffect(() => {
    if (year === "") {
      return;
    }
    const promise = onClickReadSales(year);
    console.log(promise);
    let array = [];
    let arrayDepartment = [];
    let arrayYear = [];
    let arraySales = [];

    promise.then((data) => {
      if (data.length > 0) {
        console.log(data);
        arrayDepartment.push("deparment");
        arrayYear.push("year");
        arraySales.push("sales");
        for (let i = 0; i < data.length; i++) {
          arrayDepartment.push(data[i].department);
          arrayYear.push(data[i].year);
          arraySales.push(data[i].sales);
        }
        array.push(arrayDepartment);
        array.push(arrayYear);
        array.push(arraySales);
        console.log(array);
        handleDataChange(array);
      } else {
        console.log("データベースにその年のデータがありません。");
        handleDataChange(array);
      }
    });
  }, [year]);
  return <div></div>;
};

export default ReadDatabase;
