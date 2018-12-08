// informed by the work of Josh Yuan and Nick Jaczko 
// https://github.com/joshyuan1/JuniorLints/blob/master/client/src/FileUpload.js
import React, { Component } from 'react';
import {Input, Form} from 'reactstrap';


class ImageDecode extends Component {
  constructor(props) {
    super(props);


    this.state = {
      imageurl: '',
    };
  }

  handleChange(file) {
    console.log(file.name);
    let contents;

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
        {this.state.imageurl && (<img src={this.state.imageurl}/>)}
      </Form>
    );
  }
}


export default ImageDecode;
