import axios from "axios";

export const useUpdateSales = () => {
  const endpoint = "http://127.0.0.1:8000/sales";

  const onSubmitUpdateSales = (data) => {
    const queries = {
      department: data.department,
      year: Number(data.year),
      sales: Number(data.sales),
    };
    console.log(data);
    axios
      .put(endpoint, queries)
      .then((res) => {
        console.log(res);
      })
      .catch((e) => {
        console.log(e);
      });
  };
  return { onSubmitUpdateSales };
};
