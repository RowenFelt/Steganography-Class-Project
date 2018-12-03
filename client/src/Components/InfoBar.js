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
import React from 'react';
import { TabContent, TabPane, Nav, NavItem, NavLink, Card, Button, CardTitle, CardText, Row, Col, Form, FormGroup,
  Label, Input, CardImg, CardBody, CardGroup, CardSubtitle } from 'reactstrap';
import ImageUpload from './imageupload.js'
import classnames from 'classnames';
import julia from './Images/Julia.JPG';

export default class InfoBar extends React.Component {
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      activeTab: '1'
    };
  }

  toggle(tab) {
    if (this.state.activeTab !== tab) {
      this.setState({
        activeTab: tab
      });
    }
  }
  render() {
    return (
      <div>
        <Nav tabs>
          <NavItem>
            <NavLink
              className={classnames({ active: this.state.activeTab === '1' })}
              onClick={() => { this.toggle('1'); }}
            >
              About
            </NavLink>
          </NavItem>
          <NavItem>
            <NavLink
              className={classnames({ active: this.state.activeTab === '2' })}
              onClick={() => { this.toggle('2'); }}
            >
              Encode Image
            </NavLink>
          </NavItem>
          <NavItem>
            <NavLink
              className={classnames({ active: this.state.activeTab === '3' })}
              onClick={() => { this.toggle('3'); }}
            >
              Decode Image
            </NavLink>
          </NavItem>
          <NavItem>
            <NavLink
              className={classnames({ active: this.state.activeTab === '4' })}
              onClick={() => { this.toggle('4'); }}
            >
              Team
            </NavLink>
          </NavItem>
          <NavItem>
            <NavLink
              className={classnames({ active: this.state.activeTab === '5' })}
              onClick={() => { this.toggle('5'); }}
            >
              Contact Us
            </NavLink>
          </NavItem>
        </Nav>
        <TabContent activeTab={this.state.activeTab}>
          <TabPane tabId="1">
            <Row>
              <Col sm="12">
              <br />
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
              </Col>
            </Row>
          </TabPane>
          <TabPane tabId="2">
            <Row>
              <Col sm="12">
                <br/ >
                <Form align = "left">
                <p><b>Choose an image as the base image:</b></p>
                <ImageUpload
                  callback={(userCode, userOutput) => this.setState({ pyCode: userCode, linterOutput: userOutput, mode: 'view' })}
                  startLoad={() => this.setState({ mode: 'loading' })}/>
                <p><b>Choose an image as the image to be hidden:</b></p>
                <ImageUpload
                  callback={(userCode, userOutput) => this.setState({ pyCode: userCode, linterOutput: userOutput, mode: 'view' })}
                  startLoad={() => this.setState({ mode: 'loading' })}/>
                </Form>
              </Col>
            </Row>
          </TabPane>
          <TabPane tabId="3">
            <Row>
              <Col sm="12">
                <br/ >
                <Form align="left">
                <p><b>Choose an image to be decoded:</b></p>
                <ImageUpload
                  callback={(userCode, userOutput) => this.setState({ pyCode: userCode, linterOutput: userOutput, mode: 'view' })}
                  startLoad={() => this.setState({ mode: 'loading' })}/>
                </Form>
              </Col>
            </Row>
          </TabPane>
          <TabPane tabId="4">
          <CardGroup>
            <Card>
              <CardImg top width="100%" src={julia} alt="Card image cap" />
              <CardBody>
                <CardTitle>Julia Athayde</CardTitle>
                <CardSubtitle>Computer Science & Economics '19'</CardSubtitle>
                <CardText>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</CardText>
              </CardBody>
            </Card>
            <Card>
              <CardImg top width="100%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=256%C3%97180&w=256&h=180" alt="Card image cap" />
              <CardBody>
                <CardTitle>Casey Astiz</CardTitle>
                <CardSubtitle>Computer Science & Economics '19</CardSubtitle>
                <CardText>This card has supporting text below as a natural lead-in to additional content.</CardText>
              </CardBody>
            </Card>
            <Card>
              <CardImg top width="100%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=256%C3%97180&w=256&h=180" alt="Card image cap" />
              <CardBody>
                <CardTitle>Rowen Felt</CardTitle>
                <CardSubtitle>Computer Science '19</CardSubtitle>
                <CardText>This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</CardText>
              </CardBody>
            </Card>
            </CardGroup>
          </TabPane>
          <TabPane tabId="5">
            <Row>
              <Col sm="12">
              <Form align = "left">
                <FormGroup>
                  <Label for="exampleName"><b>Name</b></Label>
                  <Input type="email" name="user_name" id="exampleName" placeholder="Your name" />
                </FormGroup>
                <FormGroup>
                  <Label for="exampleEmail"><b>Email</b></Label>
                  <Input type="email" name="email" id="exampleEmail" placeholder="Insert your email here" />
                </FormGroup>
                <FormGroup>
                  <Label for="exampleText"><b>Ask Us A Question</b></Label>
                  <Input type="textarea" name="text" id="exampleText" />
                </FormGroup>
                <Button> Submit </Button>
              </Form>
              </Col>
            </Row>
          </TabPane>
        </TabContent>
      </div>
    );
  }
}
