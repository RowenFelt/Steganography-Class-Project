import React, { Component } from 'react';
import styled from 'styled-components';
import { Button, ButtonToolbar } from 'react-bootstrap';
import InfoBar from './components/InfoBar';
import './App.css';


const Title = styled.h1`
  text-align: center
`;

class App extends Component {
  render() {

    return (
      <div className="App">
        <Title>Steganography Project - The Encoder</Title>
        <InfoBar />
        <br>
        </br>
        <ButtonToolbar>
          <Button variant = "info">Encode Image</Button>
          <Button variant = "info">Decode Image</Button>
        </ButtonToolbar>

      </div>
    );
  }
}

export default App;