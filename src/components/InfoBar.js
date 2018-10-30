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
import { Tabs, Tab } from 'react-bootstrap';


class InfoBar extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      key: 'home',
    };
  }

  render() {
    return (
      <Tabs
        id="info-bar"
        activeKey={this.state.key}
        onSelect={key => this.setState({ key })}
      >
        <Tab eventKey="home" title="Home">
          <p1 />
        </Tab>
        <Tab eventKey="about" title="About">
          <p1 />
        </Tab>
        <Tab eventKey="team" title="Team">
          <p1 />
        </Tab>
        <Tab eventKey="contact" title="Contact Us">
          <p1 />
        </Tab>
      </Tabs>
    );
  }
}

export default InfoBar;
