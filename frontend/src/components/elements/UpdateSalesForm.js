import React, { useState } from "react";
import {
  Box,
  FormControl,
  InputLabel,
  Input,
  Button,
  MenuItem,
  Select,
} from "@mui/material";
import { useUpdateSales } from "../hooks/useUpdateSales";

export const UpdateSalesForm = () => {
  const { onSubmitUpdateSales } = useUpdateSales();

  const [formData, setFormData] = useState({
    year: "",
    department: "",
    sales: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmitUpdateSales(formData);
    console.log(formData);
  };

  return (
    <Box sx={{ mt: 2, width: "100%" }}>
      <form onSubmit={handleSubmit}>
        <FormControl fullWidth>
          <InputLabel id="year-input">Year</InputLabel>
          <Select
            labelId="year"
            id="year"
            name="year"
            value={formData.year}
            label="year"
            onChange={handleChange}
          >
            <MenuItem value={2020}>2020</MenuItem>
            <MenuItem value={2021}>2021</MenuItem>
            <MenuItem value={2022}>2022</MenuItem>
          </Select>
        </FormControl>
        <FormControl fullWidth>
          <InputLabel id="department-input">Department</InputLabel>
          <Select
            labelId="department"
            id="department"
            name="department"
            value={formData.department}
            label="department"
            onChange={handleChange}
          >
            <MenuItem value={"第１営業部"}>第１営業部</MenuItem>
            <MenuItem value={"第２営業部"}>第２営業部</MenuItem>
            <MenuItem value={"第３営業部"}>第３営業部</MenuItem>
          </Select>
        </FormControl>
        <FormControl fullWidth sx={{ mb: 2 }}>
          <InputLabel htmlFor="sales-input">Sales</InputLabel>
          <Input
            id="sales"
            name="sales"
            value={formData.sales}
            onChange={handleChange}
            type="number"
          />
        </FormControl>
        <Button type="submit" variant="contained" color="primary">
          Update
        </Button>
      </form>
    </Box>
  );
};
