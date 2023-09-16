import { useState, useEffect } from "react";
import axios from "axios";

function Image(props) {
  const [data, setData] = useState(null);

  useEffect(() => {
    params = URLSearchParams([["image_query", props.query]]);
    axios
      .get("http://127.0.0.1:5000/image_search")
      .then((response) => {
        const res = response.data;
        setData({
          image: res.image,
        });
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  });

  return (
    <>
      <div className="image-container">
        {data && data.image && <img src={data.image} alt="Image" id="image" />}
      </div>
    </>
  );
}

export default Image;
