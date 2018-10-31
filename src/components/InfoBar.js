/*
  InfoBar displays the list of sections (first letter) for the collection of
  articles passed down in its props. Clicking on one of these sections displays
  a list of the available titles in that current section.

  props:
    collection: A Map of articles keyed by section
    select: A callback when article is selected
    currentArticle: Current selected article
*/

/* eslint no-underscore-dangle: [2, { "allow": ["_id"] }] */

import React, { Component } from 'react';
import { Tabs, Tab, Button, ButtonToolbar } from 'react-bootstrap';
import { Form, FormGroup, Label, Input, FormText } from 'reactstrap';
import { Card, CardImg, CardTitle, CardText, CardGroup, CardSubtitle, CardBody, CardDeck } from 'reactstrap';
import { UncontrolledCarousel } from 'reactstrap';

class InfoBar extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      key: 'home',
    };
  }

  render() {
    const items = [
      {
        src: 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa1d%20text%20%7B%20fill%3A%23555%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa1d%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23777%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22285.921875%22%20y%3D%22218.3%22%3EFirst%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
        altText: 'Slide 1',
        caption: 'Slide 1',
        header: 'Slide 1 Header'
      },
      {
        src: 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa20%20text%20%7B%20fill%3A%23444%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa20%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23666%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22247.3203125%22%20y%3D%22218.3%22%3ESecond%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
        altText: 'Slide 2',
        caption: 'Slide 2',
        header: 'Slide 2 Header'
      },
      {
        src: 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa21%20text%20%7B%20fill%3A%23333%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa21%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23555%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22277%22%20y%3D%22218.3%22%3EThird%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
        altText: 'Slide 3',
        caption: 'Slide 3',
        header: 'Slide 3 Header'
      }
    ];
    return (
      <Tabs
        id="info-bar"
        activeKey={this.state.key}
        onSelect={key => this.setState({ key })}
      >
        <Tab eventKey="home" title="Home">
          <UncontrolledCarousel items={items} />
          <br />
          <ButtonToolbar>
            <Button variant = "info">Encode Image</Button>
            <Button variant = "info">Decode Image</Button>
          </ButtonToolbar>

        </Tab>
        <Tab eventKey="about" title="About">
          <br/>
          <p align="left">This project is designed to fulfill a requirement of CS0452 - Image Processing,
          a computer science course at Middlebury College. The process of building the
          steganography coder and decoder required application of acquired knowledge of
          image processing as well as general programming and software development skills.</p>
          <p align="left">Steganography is the practice of concealing a file, message, image, or video within
          another file, message, image, or video. The word steganography combines the Greek
          words steganos, meaning "covered,concealed, or protected", and graphein meaning "writing".</p>
          <p align="left">The project aims to “hide” one image inside of another, which are given by the user. Given
          one image, we decode the image to see what may be “hidden” within said image. Through these
          two processing steps, we learned about bit manipulation in regards to images, as well as
          understood more about the granularity of images (and how that is stored).</p>
          <p align="left">Moreover, the streaming hidden image detector detects which image has a valid image hidden
          within it. A valid image here is defined as anything other than random noise.</p>
          <p align="left">In order to work on this project, we have created our own data set of images using our encoder.
          Once the encoder was set up, we created our own data set of combined images. That was accomplished
          through taking sets of other images and encoding them. We used our data set to test our decoder as
          well as our streaming hidden image detector. Images are decoded and automatically classified as
          containing a hidden image or not based on some process separating images of random noise from real
          images by way of noise detection, edge detection, or some other process.</p>
          <p align="left">We have built our steganographic systems from scratch, so we only used linraries such as be numpy,
          scikit image. There were several steganographic algorithms that could have been used to obscure an
          image within another image. All of them take advantage of high frequency noise within an image that
          can be modified without an observable change. The algorithm we will be using is based on storing a
          low resolution image (the hidden image) inside a higher resolution image (the base image) by flipping
          the least significant bits of adjacent values in the base image to represent pixel intensities of the
          hidden image. Flipping the least significant bit of a given pixel intensity can only change the color of
          that pixel by one hue, which is an imperceptibly change in color in a high frequency image with substantial
          color variation. To decode the 1 image, the least significant bits of adjacent pixels are concatenated
          together to represent the pixel intensities or RGB color values of the hidden images pixels.</p>
        </Tab>
        <Tab eventKey="team" title="Team">
        <CardDeck>
          <Card>
            <CardImg top width="30%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=256%C3%97180&w=256&h=180" alt="Card image cap" />
            <CardBody>
              <CardTitle>Julia</CardTitle>
              <CardSubtitle>CS Major '19</CardSubtitle>
              <CardText>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</CardText>
            </CardBody>
          </Card>
          <Card>
            <CardImg top width="30%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=256%C3%97180&w=256&h=180" alt="Card image cap" />
            <CardBody>
              <CardTitle>Rowen</CardTitle>
              <CardSubtitle>CS Major '19</CardSubtitle>
              <CardText>This card has supporting text below as a natural lead-in to additional content.</CardText>
            </CardBody>
          </Card>
          <Card>
            <CardImg top width="30%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=256%C3%97180&w=256&h=180" alt="Card image cap" />
            <CardBody>
              <CardTitle>Casey</CardTitle>
              <CardSubtitle>CS Major '19</CardSubtitle>
              <CardText>This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</CardText>
            </CardBody>
          </Card>
        </CardDeck>
        </Tab>
        <Tab eventKey="contact" title="Contact Us">
          <Form align="left">
            <FormGroup>
              <Label for="exampleEmail">Email</Label>
              <Input type="email" name="email" id="exampleEmail" placeholder="Insert your email" />
            </FormGroup>
            <FormGroup>
              <Label for="exampleText">Question</Label>
              <Input type="textarea" name="text" id="exampleText" />
            </FormGroup>
          </Form>
          <p1 />
        </Tab>
      </Tabs>
    )
  }
}

export default InfoBar;
