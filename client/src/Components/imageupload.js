// Initial code from GitHub
// https://gist.github.com/AshikNesin/e44b1950f6a24cfcd85330ffc1713513

import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {Input, Form} from 'reactstrap';


class ImageUpload extends Component {
  constructor(props) {
    super(props);


    this.state = {
      message: '',
      imageurl: '',
    };
  }

  handleChange(file) {
    console.log(file.name);
    this.props.startLoad();
    let contents;
    const callbackProp = this.props.callback;


    const reader = new FileReader();
    reader.readAsArrayBuffer(file);
    reader.onloadend = () => {
      contents = reader.result;

      const request = new Request(
        '/decode',
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
        });
    };
  }


  render() {
    const uploadButton = <Input type="file" id="file" placeholder="Encode" onChange={e => this.handleChange(e.target.files[0], this.props)} />;

    return (
      <Form>
        {uploadButton}
        <h1 align="center" >{this.state.message}</h1>
        {
          this.state.imageurl && (<img src={this.state.imageurl}/>)
        }
      </Form>
    );
  }
}

ImageUpload.propTypes = {
  callback: PropTypes.func.isRequired,
  startLoad: PropTypes.func.isRequired,
};

export default ImageUpload;
