import React from "react";
import axios from "axios";

export const useCreateSales = () => {
  const endpoint = "http://127.0.0.1:8000/sales";
  const onClickCreateSales = (data) => {
    console.log(data);
    console.log(data[0]);
    for (let i = 1; i < data[0].length; i++) {
      const queries = {
        department: data[0][i],
        year: Number(data[1][i]),
        sales: Number(data[2][i]),
      };
      axios
        .post(endpoint, queries)
        .then((res) => {
          if (Object.keys(res.data).length > 0) {
            console.log("登録成功");
          } else {
            console.log("登録失敗");
          }
        })
        .catch((e) => {
          console.log(e);
        });
    }
  };
  return { onClickCreateSales };
};
