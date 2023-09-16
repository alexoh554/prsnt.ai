import React from "react";
import "./index.css";
import SLIDE1 from "./slide templates/slide 1";
export default class SLIDE_MANAGER extends React.Component {
  render() {
    return (
      <div className="border_constraints">
        <SLIDE1 />
      </div>
    );
  }
}
