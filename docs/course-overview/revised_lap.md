# Learning and Assessment Plan - Robotics Programming Course

## ICTPRG430 (Apply introductory object-oriented language skills) + ICTPRG439 (Use pre-existing components)

---

## Course Overview

**Duration:** 18 sessions (4 hours each, weekly delivery)  
**Focus:** Object-oriented programming mastery and component reuse in robotics context  
**Language:** Python throughout  
**Platform:** Webots simulation with ROS integration for component demonstration  
**Assessment:** Portfolio-based with pass/fail requirements

---

## Learning and Assessment Schedule

### Phase 1: Programming Fundamentals (Sessions 1-3)

| Session | Element | Topic & Focus | Learning Resources* | Structured out of class activities* | Hours |
|---------|---------|---------------|-------------------|-----------------------------------|-------|
| **[Week 1](sessions/session-01.md)** **(4hrs)** | ICTPRG430 Element 3.1 | **Unit Testing Foundations & Binary Search**<br/>*Focus:* Test-driven development mindset, algorithmic thinking | Exercism Platform, pytest documentation | Complete Binary Search exercise with comprehensive test suite | 2 |
| **[Week 2](sessions/session-02.md)** **(4hrs)** | ICTPRG430 Element 3.1 | **Advanced Testing & Algorithmic Challenges**<br/>*Focus:* Complex testing scenarios, debugging techniques | Exercism Platform, Python debugging tools | Complete additional algorithmic challenges with full test coverage | 3 |
| **[Week 3](sessions/session-03.md)** **(4hrs)** | ICTPRG430 Element 3.1 | **Professional Testing & Development Environment**<br/>*Focus:* Industry testing practices, debugging tools mastery | Python debugger documentation, IDE setup guides, testing frameworks | Practice advanced debugging exercises, finalize development environment | 2 |

### Phase 2: Object-Oriented Programming Theory (Sessions 4-7)

| Session                                         | Element               | Topic & Focus                                                                                                            | Learning Resources*                                             | Structured out of class activities*                                     | Hours |
| ----------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ----------------------------------------------------------------------- | ----- |
| **[Week 4](sessions/session-04.md)** **(4hrs)** | ICTPRG430 Element 2.1 | **Object Model & Class Fundamentals**<br/>*Focus:* Classes, objects, instantiation, instance variables/methods           | OOP programming fundamentals, class design principles           | Implement basic Robot class hierarchy with proper encapsulation         | 3     |
| **[Week 5](sessions/session-05.md)** **(4hrs)** | ICTPRG430 Element 2.1 | **Advanced Class Features & Magic Methods**<br/>*Focus:* Properties, class methods, magic methods, operators             | Python magic methods documentation, operator overloading guides | Implement Robot class with full magic method suite and operators        | 3     |
| **[Week 6](sessions/session-06.md)** **(4hrs)** | ICTPRG430 Element 2.1 | **Inheritance & Polymorphism Mastery**<br/>*Focus:* Class inheritance, super(), method resolution, polymorphic behaviors | Inheritance design patterns, polymorphism examples              | Design complete robot inheritance hierarchy with polymorphic interfaces | 4     |
| **[Week 7](session-07.md)** **(4hrs)** | ICTPRG430 Element 2.2 | **File I/O & Documentation Standards**<br/>*Focus:* File operations, JSON/XML parsing, professional documentation        | Python file handling documentation, docstring conventions       | Implement configuration system with comprehensive documentation         | 3     |

!!! warning "Portfolio 1 Assessment Point"
    **AT Task 1 - OOP Fundamentals Portfolio** (Due end of Week 7)

### Phase 3: Applied OOP Robotics (Sessions 8-12)

| Session                                          | Element                   | Topic & Focus                                                                                                   | Learning Resources*                                | Structured out of class activities*                                 | Hours |
| ------------------------------------------------ | ------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------- | ----- |
| **[Week 8](sessions/session-08.md)** **(4hrs)**  | ICTPRG430 Element 1.1     | **Felipe Lab 1 OOP Refactoring**<br/>*Focus:* Convert procedural robot movement to class-based architecture     | Felipe Martins Lab 1, Webots Python API            | Refactor Lab 1 using OOP principles with unit test integration      | 3     |
| **[Week 9](sessions/session-09.md)** **(4hrs)**  | ICTPRG430 Element 2.1     | **Felipe Lab 2 OOP Implementation**<br/>*Focus:* Inheritance and sensor processing with line-following behavior | Felipe Martins Lab 2, sensor processing algorithms | Implement line-following robot with proper inheritance hierarchy    | 4     |
| **[Week 10](sessions/session-10.md)** **(4hrs)** | ICTPRG430 Element 2.1     | **Felipe Lab 3 OOP Navigation**<br/>*Focus:* Polymorphism and localization systems using OOP design             | Felipe Martins Lab 3, localization algorithms      | Create odometry-based navigation system with polymorphic interfaces | 4     |
| **[Week 11](sessions/session-11.md)** **(4hrs)** | ICTPRG430 Element 3.1     | **Felipe Lab 4 OOP Control Systems**<br/>*Focus:* Advanced algorithms and testing in object-oriented framework  | Felipe Martins Lab 4, PID control theory           | Implement PID controller system with comprehensive testing          | 3     |
| **[Week 12](sessions/session-12.md)** **(4hrs)** | ICTPRG430 Element 4.1-4.2 | **Felipe Lab 5 OOP Mission Integration**<br/>*Focus:* Complete system integration and user acceptance           | Felipe Martins Lab 5, behavior coordination        | Complete mission-based robot system with full documentation         | 4     |

!!! warning "Portfolio 1 Assessment Point"
    **AT Task 2-5 - Applied OOP Robotics Portfolio** (Due progressively through Weeks 8-12)

### Phase 4: Component Research & Analysis (Sessions 13-15)

| Session | Element | Topic & Focus | Learning Resources* | Structured out of class activities* | Hours |
|---------|---------|---------------|-------------------|-----------------------------------|-------|
| **[Week 13](sessions/session-13.md)** **(4hrs)** | ICTPRG439 Element 1.1-1.2 | **ROS Component Analysis & Research**<br/>*Focus:* Component identification, functionality analysis, source evaluation | ROS package documentation, Mastering ROS Chapter 5 | Research ROS packages for line-following robot enhancement | 4 |
| **[Week 14](sessions/session-14.md)** **(4hrs)** | ICTPRG439 Element 2.1-2.4 | **Component Evaluation & Selection**<br/>*Focus:* Suitability assessment, licensing analysis, cost evaluation | Open source licensing guides, cost analysis methodologies | Complete formal component evaluation matrix for selected ROS packages | 3 |
| **[Week 15](sessions/session-15.md)** **(4hrs)** | ICTPRG439 Element 2.5-3.1 | **Integration Planning & Environment Setup**<br/>*Focus:* Technical impact analysis, ROS-Webots development environment | Mastering ROS Chapter 5, ROS-Webots integration documentation | Set up ROS-Webots integrated development environment | 3 |

### Phase 5: Component Integration Implementation (Sessions 16-17)

| Session | Element | Topic & Focus | Learning Resources* | Structured out of class activities* | Hours |
|---------|---------|---------------|-------------------|-----------------------------------|-------|
| **[Week 16](sessions/session-16.md)** **(4hrs)** | ICTPRG439 Element 3.2-3.4 | **ROS Component Integration - Line Follower**<br/>*Focus:* Test program development, incremental integration, dependency resolution | Selected ROS component documentation, integration examples | **In-class development only** - ROS integration with line-following robot | 0 |
| **[Week 17](sessions/session-17.md)** **(4hrs)** | ICTPRG439 Element 3.5-3.6 | **System Assembly & Documentation**<br/>*Focus:* Final system testing, issue resolution, professional documentation | Professional documentation templates, ROS best practices | **In-class development only** - Complete system documentation and validation | 0 |

!!! success "Portfolio 2 Assessment Point"
    **ICTPRG439 Component Integration Portfolio** (Due end of Week 17)

### Phase 6: Assessment & Completion (Session 18)

| Session | Element | Topic & Focus | Learning Resources* | Structured out of class activities* | Hours |
|---------|---------|---------------|-------------------|-----------------------------------|-------|
| **[Week 18](sessions/session-18.md)** **(4hrs)** | Both Units | **Portfolio Review & Competency Validation**<br/>*Focus:* Final competency demonstration, portfolio completion, resit opportunities | Course materials review, industry standards reference | Review and complete any outstanding portfolio items | 2 |

---

## Quick Navigation

- **Resources:** [Downloads & Materials](downloads.md)
- **Assessment:** [Portfolio Requirements](assessment.md)  
- **Reference:** [Course Glossary](glossary.md)

---

*\* Learning Resources and Structured Activities detailed in individual session pages*