import React, { useContext } from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import BasicMenu from "../elements/BasicMenu";
import { Grid } from "@mui/material";
import { LoginUserContext } from "../providers/LoginUserProvider";

const Header = (props) => {
  const { loginUser } = useContext(LoginUserContext);
  return (
    <AppBar position="static">
      <Toolbar>
        <Grid container>
          <Grid item xs={6}>
            <BasicMenu />
          </Grid>
          <Grid item xs={6} sx={{ py: 1 }}>
            {props.name}
            <Typography variant="p" component="div" sx={{ flexGrow: 1 }}>
              ログインユーザ：{loginUser}
            </Typography>
          </Grid>
        </Grid>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
