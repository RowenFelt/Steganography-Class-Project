// Initial code from GitHub
// https://gist.github.com/AshikNesin/e44b1950f6a24cfcd85330ffc1713513

import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Input, Form, FormGroup } from 'reactstrap';


class ImageEncode extends Component {
  constructor(props) {
    super(props);


    this.state = {
      message: '',
      imageurl: '',
    };
  }

  firstFileHandler(file) {
    console.log(file.name);
    this.props.startLoad();
    let contents;
    const callbackProp = this.props.callback;


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
    this.props.startLoad();
    let contents;
    const callbackProp = this.props.callback;


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
        <p><b>Choose an image as the base image:</b></p>
        {uploadButtonBase}
        <p><b>Choose an image to be hidden:</b></p>
        {uploadButtonHidden}
        <h1 align="center" >{this.state.message}</h1>
        {
          this.state.imageurl && (<img src={this.state.imageurl}/>)
        }
        </div>
    );
  }
}

ImageEncode.propTypes = {
  callback: PropTypes.func.isRequired,
  startLoad: PropTypes.func.isRequired,
};

export default ImageEncode;
