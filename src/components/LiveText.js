import React from "react";

const LiveText = (props) => {
    return (
        <div className="live_text">
            <p>{props.text}</p>
        </div>
    );
}

export default LiveText;