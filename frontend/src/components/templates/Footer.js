import React from "react";
import Typography from "@mui/material/Typography";

const Copyright = (props) => {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      {"Copyright © "}
      ABCD corp.
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
};

export const Footer = () => {
  return (
    <>
      <Copyright sx={{ mt: 8, mb: 4 }} />
    </>
  );
};
