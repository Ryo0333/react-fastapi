import React from "react";
import Papa from "papaparse";
import ReactFileReader from "react-file-reader";
import { Button } from "@mui/material";
import { useCreateSales } from "../hooks/useCreateSales";

const ReadCsv = (props) => {
  const { handleDataChange } = props;
  const { onClickCreateSales } = useCreateSales();
  const uploadFile = (files) => {
    Papa.parse(files[0], {
      skipEmptyLines: true,
      complete: function (results) {
        console.log(results);
        onClickCreateSales(results.data);
        handleDataChange(results.data);
      },
    });
  };
  return (
    <>
      <ReactFileReader handleFiles={uploadFile} fileTypes={".csv"}>
        <Button variant="contained">Upload</Button>
      </ReactFileReader>
    </>
  );
};

export default ReadCsv;
