import React from "react";
import "./index.css";
import SLIDE1 from "./slide templates/slide 1";
import { ReactMic } from "react-mic";

async function speechblob_to_gcloud(recordedBlob) {
  let response = await fetch("http://localhost:5000/speechblob_to_gcloud", {
    method: "POST",
    body: recordedBlob,
  });
  //response = await response.json();
}

export default class SLIDE_MANAGER extends React.Component {
  state = {
    record: false,
  };

  startRecording = () => {
    this.setState({ record: true });
  };

  stopRecording = () => {
    this.setState({ record: false });
  };

  onData(recordedBlob) {
    console.log("chunk of real-time data is: ", recordedBlob);
    speechblob_to_gcloud(recordedBlob);
  }

  onStop(recordedBlob) {
    console.log("recordedBlob is: ", recordedBlob);
  }
  render() {
    return (
      <div className="border_constraints">
        <SLIDE1 />
        <ReactMic
          record={this.state.record}
          onStop={this.onStop}
          onData={this.onData}
          mimeType="audio/webm"
          timeSlice={20000}
        />
        <button onClick={this.startRecording} type="button">
          Start
        </button>
        <button onClick={this.stopRecording} type="button">
          Stop
        </button>
      </div>
    );
  }
}
