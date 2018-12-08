// informed by the work of Josh Yuan and Nick Jaczko 
// https://github.com/joshyuan1/JuniorLints/blob/master/client/src/FileUpload.js

import React, { Component } from 'react';
import {Input} from 'reactstrap';


class ImageEncode extends Component {
  constructor(props) {
    super(props);


    this.state = {
      imageurl: '',
    };
  }

  firstFileHandler(file) {
    console.log(file.name);
    let contents;

    const reader = new FileReader();
    reader.readAsArrayBuffer(file);
    reader.onloadend = () => {
      contents = reader.result;

      const request = new Request(
        '/encodefirst',
        {
          method: 'POST',
          body: contents,
        },
      );

      fetch(request)
        .then((response) => {
          if (!response.ok) {
            throw new Error(response.status_text);
          }
          return response.json();
        })
        .then((jsonurl) => {
          console.log(jsonurl);
        });
    };
  }

  secondFileHandler(file) {
    console.log(file.name);
    let contents;

    const reader = new FileReader();
    reader.readAsArrayBuffer(file);
    reader.onloadend = () => {
      contents = reader.result;

      const request = new Request(
        '/encodesecond',
        {
          method: 'POST',
          body: contents,
        },
      );

      fetch(request)
        .then((response) => {
          if (!response.ok) {
            throw new Error(response.status_text);
          }
          return response.json();
        })
        .then((jsonurl) => {
          this.setState({imageurl: jsonurl.url});
          console.log(jsonurl.url);
        });
    };
  }

  render() {
     const uploadButtonBase = <Input type="file" id="file1" placeholder="Encode" onChange={e => this.firstFileHandler(e.target.files[0], this.props)} />;

   const uploadButtonHidden = <Input type="file" id="file2" placeholder="Encode" onChange={e => this.secondFileHandler(e.target.files[0], this.props)} />;

    return (
      <div>
        <p> Upload a base image </p>
        {uploadButtonBase}
        <p> Upload an image to encode</p>
        {uploadButtonHidden}
        {this.state.imageurl && (<img src={this.state.imageurl}/>)}
      </div>
    );
  }
}


export default ImageEncode;
