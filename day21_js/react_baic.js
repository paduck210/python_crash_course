import React, {Componet} from 'react';
import ReactDOM from 'react-dom';



// change X => props
const Hello = (props) => {
  return <div>Hello, {props.name}</div>
}
const root = document.getElementById('root');
if (root) {
  ReactDOM.render(
    <Hello name="Boris" />,
    root);
}


// change O => state
class Hello extends Componet {
  constructor(props) {
    super(this.props);

    this.state = {
      clicked: false,
      counter: 0
    };
  }

  handleClick = () => {
    this.setState({
      clicked: !this.state.clicked,
      counter: this.state.counter + 1
    });
  }

  render() {
    return (
      <div className={this.state.clicked ? 'clicked' : null},
      onclick={this.handleClick}>
        Hello, {this.props.name} {this.state.counter}
      </div>
    )
  }
}
