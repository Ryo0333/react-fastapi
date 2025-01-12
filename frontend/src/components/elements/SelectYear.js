import React from "react";
import { Box, InputLabel, MenuItem, Select } from "@mui/material";

const SelectYear = (props) => {
  const { handleYearChange } = props;
  const handleChange = (e) => {
    handleYearChange(e.target.value);
  };
  return (
    <>
      <Box sx={{ mt: 2, width: "100%" }}>
        <InputLabel id="sales-year">年度</InputLabel>
        <Select
          labelId="sales-year"
          onChange={handleChange}
          fullWidth
          name="year"
          defaultValue={""}
        >
          <MenuItem value={2020}>2020</MenuItem>
          <MenuItem value={2021}>2021</MenuItem>
          <MenuItem value={2022}>2022</MenuItem>
        </Select>
      </Box>
    </>
  );
};

export default SelectYear;
