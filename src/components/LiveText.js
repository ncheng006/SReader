import React from "react";


const LiveText = (props) => {
    return (
        <div className="left-column">
            <div className="text-area">
                <p className="live-text">{props.text}</p>
            </div>
            <div className="level-bar-container">
                <div className="level-bar"
                    style={{ width: props.width + "%", backgroundColor: "green" }}
                />
                <div className="level-bar"
                    style={{ width: 100 - props.width + "%" }}
                />
            </div>
        </div>
    );
}

export default LiveText;