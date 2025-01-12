import axios from "axios";
import React from "react";

export const useReadSales = () => {
  const baseEndpoint = "http://127.0.0.1:8000/sales/";

  const onClickReadSales = async (year) => {
    const endpoint = baseEndpoint + year;
    const res = await axios.get(endpoint);
    return res.data;
  };
  return { onClickReadSales };
};
