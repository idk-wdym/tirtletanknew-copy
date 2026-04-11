from manim import *

# Configure global settings for the scene
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.background_color = WHITE

class GeneratedScene(Scene):
    def construct(self):
        # --- Scene 1: Title and Introduction ---
        self.camera.background_color = WHITE

        title = MathTex(r"\text{Electronic Configuration}", color=BLUE_D, font_size=96)
        self.play(Write(title))
        self.wait(1)

        definition_text = MathTex(
            r"\text{The arrangement of electrons in atomic orbitals.}",
            color=BLACK,
            font_size=60
        ).next_to(title, DOWN, buff=1.0)
        self.play(FadeIn(definition_text, shift=UP))
        self.wait(2)

        importance_text = MathTex(
            r"\text{Determines an atom's chemical properties and reactivity.}",
            color=GRAY_D,
            font_size=48
        ).next_to(definition_text, DOWN, buff=0.5)
        self.play(FadeIn(importance_text, shift=UP))
        self.wait(2)

        self.play(FadeOut(title, shift=UP), FadeOut(definition_text, shift=UP), FadeOut(importance_text, shift=UP))
        self.clear() # Clear the screen for the next section

        # --- Scene 2: Key Principles ---
        principles_title = MathTex(r"\text{Key Principles}", color=BLUE_D, font_size=84)
        self.play(Write(principles_title))
        self.wait(1)

        # Aufbau Principle
        aufbau_title = MathTex(r"\text{1. Aufbau Principle}", color=GREEN_D, font_size=64).to_edge(UL, buff=1.0)
        aufbau_desc = MathTex(
            r"\text{Electrons fill atomic orbitals of the lowest available energy levels }",
            r"\\ \text{before occupying higher levels.}",
            color=BLACK,
            font_size=40
        ).next_to(aufbau_title, DOWN, buff=0.5).align_to(aufbau_title, LEFT)
        self.play(FadeIn(aufbau_title, shift=LEFT), FadeIn(aufbau_desc, shift=LEFT))
        self.wait(2)

        # Visualizing Aufbau Principle (simplified energy levels)
        # Define orbital box dimensions
        box_width = 1.0
        box_height = 0.5
        box_spacing = 0.1

        # 1s orbital
        s1_label = MathTex(r"1s", color=TEAL_D, font_size=36)
        s1_box = Rectangle(width=box_width, height=box_height, color=TEAL_D, stroke_width=2)
        s1_orbital = VGroup(s1_box, s1_label).arrange(RIGHT, buff=0.2).move_to(LEFT * 4 + DOWN * 2)

        # 2s orbital
        s2_label = MathTex(r"2s", color=TEAL_D, font_size=36)
        s2_box = Rectangle(width=box_width, height=box_height, color=TEAL_D, stroke_width=2)
        s2_orbital = VGroup(s2_box, s2_label).arrange(RIGHT, buff=0.2).next_to(s1_orbital, UP, buff=1.0).align_to(s1_orbital, LEFT)

        # 2p orbital
        p2_label = MathTex(r"2p", color=TEAL_D, font_size=36)
        p2_boxes = VGroup(*[Rectangle(width=box_width, height=box_height, color=TEAL_D, stroke_width=2) for _ in range(3)]).arrange(RIGHT, buff=box_spacing)
        p2_orbital = VGroup(p2_boxes, p2_label).arrange(RIGHT, buff=0.2).next_to(s2_orbital, UP, buff=1.0).align_to(s2_orbital, LEFT)

        orbitals_group = VGroup(s1_orbital, s2_orbital, p2_orbital).shift(RIGHT * 3)
        self.play(FadeIn(orbitals_group))
        self.wait(1)

        # Simulate filling electrons
        electron_up = MathTex(r"\uparrow", color=RED_D, font_size=48)
        electron_down = MathTex(r"\downarrow", color=RED_D, font_size=48)

        # 1s
        e1 = electron_up.copy().move_to(s1_box.get_center())
        self.play(FadeIn(e1, shift=UP))
        self.wait(0.5)
        e2 = electron_down.copy().move_to(s1_box.get_center())
        self.play(FadeIn(e2, shift=DOWN))
        self.wait(1)

        # 2s
        e3 = electron_up.copy().move_to(s2_box.get_center())
        self.play(FadeIn(e3, shift=UP))
        self.wait(0.5)
        e4 = electron_down.copy().move_to(s2_box.get_center())
        self.play(FadeIn(e4, shift=DOWN))
        self.wait(1)

        # 2p
        e5 = electron_up.copy().move_to(p2_boxes[0].get_center())
        self.play(FadeIn(e5, shift=UP))
        self.wait(0.5)
        e6 = electron_up.copy().move_to(p2_boxes[1].get_center())
        self.play(FadeIn(e6, shift=UP))
        self.wait(0.5)
        e7 = electron_up.copy().move_to(p2_boxes[2].get_center())
        self.play(FadeIn(e7, shift=UP))
        self.wait(0.5)
        e8 = electron_down.copy().move_to(p2_boxes[0].get_center())
        self.play(FadeIn(e8, shift=DOWN))
        self.wait(0.5)
        e9 = electron_down.copy().move_to(p2_boxes[1].get_center())
        self.play(FadeIn(e9, shift=DOWN))
        self.wait(0.5)
        e10 = electron_down.copy().move_to(p2_boxes[2].get_center())
        self.play(FadeIn(e10, shift=DOWN))
        self.wait(1)

        self.play(FadeOut(orbitals_group, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10))
        self.wait(0.5)

        # Pauli Exclusion Principle
        pauli_title = MathTex(r"\text{2. Pauli Exclusion Principle}", color=GREEN_D, font_size=64).to_edge(UL, buff=1.0)
        pauli_desc = MathTex(
            r"\text{No two electrons in the same atom can have identical values for all four quantum numbers.}",
            r"\\ \text{An atomic orbital can hold a maximum of two electrons, which must have opposite spins.}",
            color=BLACK,
            font_size=40
        ).next_to(pauli_title, DOWN, buff=0.5).align_to(pauli_title, LEFT)

        self.play(Transform(aufbau_title, pauli_title), Transform(aufbau_desc, pauli_desc))
        self.wait(2)

        # Visualizing Pauli Principle
        pauli_box = Rectangle(width=box_width, height=box_height, color=TEAL_D, stroke_width=2).move_to(RIGHT * 3)
        pauli_label = MathTex(r"\text{Orbital}", color=TEAL_D, font_size=36).next_to(pauli_box, DOWN, buff=0.2)
        self.play(FadeIn(pauli_box, pauli_label))
        self.wait(0.5)

        e_up = electron_up.copy().move_to(pauli_box.get_center())
        self.play(FadeIn(e_up, shift=UP))
        self.wait(0.5)

        e_down = electron_down.copy().move_to(pauli_box.get_center())
        self.play(FadeIn(e_down, shift=DOWN))
        self.wait(1)

        # Incorrect example
        incorrect_box = Rectangle(width=box_width, height=box_height, color=RED_D, stroke_width=2).next_to(pauli_box, RIGHT, buff=2.0)
        incorrect_label = MathTex(r"\text{Incorrect}", color=RED_D, font_size=36).next_to(incorrect_box, DOWN, buff=0.2)
        e_up_inc1 = electron_up.copy().move_to(incorrect_box.get_center())
        e_up_inc2 = electron_up.copy().move_to(incorrect_box.get_center()) # This will overlap, showing the issue

        self.play(FadeIn(incorrect_box, incorrect_label))
        self.wait(0.5)
        self.play(FadeIn(e_up_inc1, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(e_up_inc2, shift=UP)) # This visually shows two up spins in one box
        self.wait(1)

        cross = Cross(incorrect_box, stroke_width=8, color=RED_D)
        self.play(Create(cross))
        self.wait(1)

        self.play(FadeOut(pauli_box, pauli_label, e_up, e_down, incorrect_box, incorrect_label, e_up_inc1, e_up_inc2, cross))
        self.wait(0.5)

        # Hund's Rule
        hund_title = MathTex(r"\text{3. Hund's Rule}", color=GREEN_D, font_size=64).to_edge(UL, buff=1.0)
        hund_desc = MathTex(
            r"\text{For degenerate orbitals (orbitals of the same energy), electrons fill each orbital singly }",
            r"\\ \text{before any orbital is doubly occupied. All singly occupied orbitals must have the same spin.}",
            color=BLACK,
            font_size=40
        ).next_to(hund_title, DOWN, buff=0.5).align_to(hund_title, LEFT)

        self.play(Transform(aufbau_title, hund_title), Transform(aufbau_desc, hund_desc))
        self.wait(2)

        # Visualizing Hund's Rule (p-orbitals)
        p_orbitals_hund = VGroup(*[Rectangle(width=box_width, height=box_height, color=TEAL_D, stroke_width=2) for _ in range(3)]).arrange(RIGHT, buff=box_spacing).move_to(LEFT * 3)
        p_label_hund = MathTex(r"2p \text{ Orbitals}", color=TEAL_D, font_size=36).next_to(p_orbitals_hund, DOWN, buff=0.2)
        self.play(FadeIn(p_orbitals_hund, p_label_hund))
        self.wait(0.5)

        # Correct filling (3 electrons)
        e_h1 = electron_up.copy().move_to(p_orbitals_hund[0].get_center())
        e_h2 = electron_up.copy().move_to(p_orbitals_hund[1].get_center())
        e_h3 = electron_up.copy().move_to(p_orbitals_hund[2].get_center())
        self.play(FadeIn(e_h1, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(e_h2, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(e_h3, shift=UP))
        self.wait(1)

        correct_label = MathTex(r"\text{Correct}", color=GREEN_D, font_size=36).next_to(p_orbitals_hund, UP, buff=0.5)
        self.play(FadeIn(correct_label))
        self.wait(1)

        # Incorrect filling (3 electrons)
        p_orbitals_incorrect = VGroup(*[Rectangle(width=box_width, height=box_height, color=RED_D, stroke_width=2) for _ in range(3)]).arrange(RIGHT, buff=box_spacing).move_to(RIGHT * 3)
        p_label_incorrect = MathTex(r"2p \text{ Orbitals}", color=RED_D, font_size=36).next_to(p_orbitals_incorrect, DOWN, buff=0.2)
        self.play(FadeIn(p_orbitals_incorrect, p_label_incorrect))
        self.wait(0.5)

        e_hi1 = electron_up.copy().move_to(p_orbitals_incorrect[0].get_center())
        e_hi2 = electron_down.copy().move_to(p_orbitals_incorrect[0].get_center())
        e_hi3 = electron_up.copy().move_to(p_orbitals_incorrect[1].get_center())

        self.play(FadeIn(e_hi1, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(e_hi2, shift=DOWN)) # Paired before filling all singly
        self.wait(0.5)
        self.play(FadeIn(e_hi3, shift=UP))
        self.wait(1)

        incorrect_label_hund = MathTex(r"\text{Incorrect}", color=RED_D, font_size=36).next_to(p_orbitals_incorrect, UP, buff=0.5)
        self.play(FadeIn(incorrect_label_hund))
        self.wait(1)

        cross_hund = Cross(p_orbitals_incorrect, stroke_width=8, color=RED_D)
        self.play(Create(cross_hund))
        self.wait(1)

        self.play(FadeOut(principles_title, aufbau_title, aufbau_desc,
                          p_orbitals_hund, p_label_hund, e_h1, e_h2, e_h3, correct_label,
                          p_orbitals_incorrect, p_label_incorrect, e_hi1, e_hi2, e_hi3, incorrect_label_hund, cross_hund))
        self.clear()

        # --- Scene 3: Orbital Types and Capacity ---
        orbital_title = MathTex(r"\text{Orbital Types and Capacity}", color=BLUE_D, font_size=84)
        self.play(Write(orbital_title))
        self.wait(1)

        # Orbital types
        s_orbital_text = MathTex(r"\text{s-orbital}", color=TEAL_D, font_size=60).shift(UP * 2 + LEFT * 4)
        s_capacity = MathTex(r"\text{Capacity: 2 electrons}", color=BLACK, font_size=40).next_to(s_orbital_text, DOWN, buff=0.5)
        s_shape = Sphere(radius=0.8, color=BLUE_A, opacity=0.6).next_to(s_capacity, DOWN, buff=0.8)
        self.play(FadeIn(s_orbital_text, shift=LEFT), FadeIn(s_capacity, shift=LEFT), Create(s_shape))
        self.wait(1.5)

        p_orbital_text = MathTex(r"\text{p-orbital}", color=TEAL_D, font_size=60).shift(UP * 2)
        p_capacity = MathTex(r"\text{Capacity: 6 electrons (3 orbitals)}", color=BLACK, font_size=40).next_to(p_orbital_text, DOWN, buff=0.5)
        p_shape_x = VGroup(
            Sphere(radius=0.4, color=RED_A, opacity=0.6).shift(LEFT * 0.5),
            Sphere(radius=0.4, color=RED_A, opacity=0.6).shift(RIGHT * 0.5)
        ).next_to(p_capacity, DOWN, buff=0.8)
        self.play(FadeIn(p_orbital_text, shift=UP), FadeIn(p_capacity, shift=UP), Create(p_shape_x))
        self.wait(1.5)

        d_orbital_text = MathTex(r"\text{d-orbital}", color=TEAL_D, font_size=60).shift(UP * 2 + RIGHT * 4)
        d_capacity = MathTex(r"\text{Capacity: 10 electrons (5 orbitals)}", color=BLACK, font_size=40).next_to(d_orbital_text, DOWN, buff=0.5)
        # Simplified d-orbital representation
        d_shape = VGroup(
            p_shape_x.copy().shift(UP * 0.5 + LEFT * 0.5),
            p_shape_x.copy().shift(DOWN * 0.5 + RIGHT * 0.5).rotate(PI/2)
        ).next_to(d_capacity, DOWN, buff=0.8)
        self.play(FadeIn(d_orbital_text, shift=RIGHT), FadeIn(d_capacity, shift=RIGHT), Create(d_shape))
        self.wait(2)

        self.play(FadeOut(orbital_title, s_orbital_text, s_capacity, s_shape,
                          p_orbital_text, p_capacity, p_shape_x,
                          d_orbital_text, d_capacity, d_shape))
        self.clear()

        # --- Scene 4: Spectroscopic Notation Example (Carbon) ---
        notation_title = MathTex(r"\text{Spectroscopic Notation}", color=BLUE_D, font_size=84)
        self.play(Write(notation_title))
        self.wait(1)

        carbon_atom = MathTex(r"\text{Carbon (C)}", color=GREEN_D, font_size=72).next_to(notation_title, DOWN, buff=1.0)
        atomic_number = MathTex(r"\text{Atomic Number (Z) = 6}", color=BLACK, font_size=48).next_to(carbon_atom, DOWN, buff=0.5)
        self.play(FadeIn(carbon_atom, shift=UP), FadeIn(atomic_number, shift=UP))
        self.wait(1.5)

        # Energy level diagram for filling
        energy_diagram_title = MathTex(r"\text{Energy Levels}", color=GRAY_D, font_size=40).to_edge(UL, buff=1.0)
        self.play(FadeIn(energy_diagram_title))

        # Simplified energy level diagram
        levels = VGroup()
        level_labels = ["1s", "2s", "2p"]
        orbital_groups = []

        for i, label in enumerate(level_labels):
            if "s" in label:
                box = Rectangle(width=box_width, height=box_height, color=TEAL_D, stroke_width=2)
                orbital_group = VGroup(box)
            elif "p" in label:
                boxes = VGroup(*[Rectangle(width=box_width, height=box_height, color=TEAL_D, stroke_width=2) for _ in range(3)]).arrange(RIGHT, buff=box_spacing)
                orbital_group = boxes
            
            level_label_mobj = MathTex(label, color=TEAL_D, font_size=36).next_to(orbital_group, LEFT, buff=0.5)
            
            if i == 0:
                orbital_group.move_to(LEFT * 4 + DOWN * 2)
            else:
                orbital_group.next_to(orbital_groups[-1], UP, buff=1.0).align_to(orbital_groups[-1], LEFT)
            
            orbital_groups.append(orbital_group)
            levels.add(VGroup(orbital_group, level_label_mobj))

        self.play(FadeIn(levels))
        self.wait(1)

        # Fill electrons for Carbon (6 electrons)
        electrons_carbon = VGroup()
        electron_count = 0

        # 1s orbital
        for _ in range(2):
            e = electron_up.copy().move_to(orbital_groups[0][0].get_center())
            if electron_count % 2 == 1:
                e.become(electron_down.copy().move_to(orbital_groups[0][0].get_center()))
            self.play(FadeIn(e, shift=UP if electron_count % 2 == 0 else DOWN), run_time=0.3)
            electrons_carbon.add(e)
            electron_count += 1
            self.wait(0.2)
        self.wait(0.5)

        # 2s orbital
        for _ in range(2):
            e = electron_up.copy().move_to(orbital_groups[1][0].get_center())
            if electron_count % 2 == 1:
                e.become(electron_down.copy().move_to(orbital_groups[1][0].get_center()))
            self.play(FadeIn(e, shift=UP if electron_count % 2 == 0 else DOWN), run_time=0.3)
            electrons_carbon.add(e)
            electron_count += 1
            self.wait(0.2)
        self.wait(0.5)

        # 2p orbital (2 electrons, Hund's rule)
        for i in range(2):
            e = electron_up.copy().move_to(orbital_groups[2][i].get_center())
            self.play(FadeIn(e, shift=UP), run_time=0.3)
            electrons_carbon.add(e)
            electron_count += 1
            self.wait(0.2)
        self.wait(1)

        # Spectroscopic notation result
        config_text = MathTex(r"\text{Electronic Configuration:}", color=BLACK, font_size=50).to_edge(RIGHT, buff=1.0).shift(UP * 2)
        carbon_config = MathTex(r"1s^2 2s^2 2p^2", color=RED_D, font_size=72).next_to(config_text, DOWN, buff=0.5).align_to(config_text, LEFT)
        self.play(FadeIn(config_text, shift=RIGHT), Write(carbon_config))
        self.wait(2)

        self.play(FadeOut(notation_title, carbon_atom, atomic_number, energy_diagram_title, levels, electrons_carbon, config_text, carbon_config))
        self.clear()

        # --- Scene 5: Orbital Diagram Example (Oxygen) ---
        orbital_diagram_title = MathTex(r"\text{Orbital Diagram Notation}", color=BLUE_D, font_size=84)
        self.play(Write(orbital_diagram_title))
        self.wait(1)

        oxygen_atom = MathTex(r"\text{Oxygen (O)}", color=GREEN_D, font_size=72).next_to(orbital_diagram_title, DOWN, buff=1.0)
        atomic_number_o = MathTex(r"\text{Atomic Number (Z) = 8}", color=BLACK, font_size=48).next_to(oxygen_atom, DOWN, buff=0.5)
        self.play(FadeIn(oxygen_atom, shift=UP), FadeIn(atomic_number_o, shift=UP))
        self.wait(1.5)

        # Orbital diagram setup
        orbital_diagram_group = VGroup()
        
        # 1s
        s1_box_o = Rectangle(width=box_width, height=box_height, color=TEAL_D, stroke_width=2)
        s1_label_o = MathTex(r"1s", color=TEAL_D, font_size=36).next_to(s1_box_o, DOWN, buff=0.2)
        s1_orbital_o = VGroup(s1_box_o, s1_label_o).shift(LEFT * 5 + UP * 1.5)
        orbital_diagram_group.add(s1_orbital_o)

        # 2s
        s2_box_o = Rectangle(width=box_width, height=box_height, color=TEAL_D, stroke_width=2)
        s2_label_o = MathTex(r"2s", color=TEAL_D, font_size=36).next_to(s2_box_o, DOWN, buff=0.2)
        s2_orbital_o = VGroup(s2_box_o, s2_label_o).next_to(s1_orbital_o, RIGHT, buff=2.0)
        orbital_diagram_group.add(s2_orbital_o)

        # 2p
        p2_boxes_o = VGroup(*[Rectangle(width=box_width, height=box_height, color=TEAL_D, stroke_width=2) for _ in range(3)]).arrange(RIGHT, buff=box_spacing)
        p2_label_o = MathTex(r"2p", color=TEAL_D, font_size=36).next_to(p2_boxes_o, DOWN, buff=0.2)
        p2_orbital_o = VGroup(p2_boxes_o, p2_label_o).next_to(s2_orbital_o, RIGHT, buff=2.0)
        orbital_diagram_group.add(p2_orbital_o)

        self.play(FadeIn(orbital_diagram_group))
        self.wait(1)

        # Fill electrons for Oxygen (8 electrons)
        electrons_oxygen = VGroup()
        electron_count_o = 0

        # 1s
        e_o1 = electron_up.copy().move_to(s1_box_o.get_center())
        e_o2 = electron_down.copy().move_to(s1_box_o.get_center())
        self.play(FadeIn(e_o1, shift=UP), run_time=0.3)
        self.play(FadeIn(e_o2, shift=DOWN), run_time=0.3)
        electrons_oxygen.add(e_o1, e_o2)
        electron_count_o += 2
        self.wait(0.5)

        # 2s
        e_o3 = electron_up.copy().move_to(s2_box_o.get_center())
        e_o4 = electron_down.copy().move_to(s2_box_o.get_center())
        self.play(FadeIn(e_o3, shift=UP), run_time=0.3)
        self.play(FadeIn(e_o4, shift=DOWN), run_time=0.3)
        electrons_oxygen.add(e_o3, e_o4)
        electron_count_o += 2
        self.wait(0.5)

        # 2p (4 electrons, Hund's rule)
        # Fill singly first
        e_o5 = electron_up.copy().move_to(p2_boxes_o[0].get_center())
        e_o6 = electron_up.copy().move_to(p2_boxes_o[1].get_center())
        e_o7 = electron_up.copy().move_to(p2_boxes_o[2].get_center())
        self.play(FadeIn(e_o5, shift=UP), run_time=0.3)
        self.play(FadeIn(e_o6, shift=UP), run_time=0.3)
        self.play(FadeIn(e_o7, shift=UP), run_time=0.3)
        electrons_oxygen.add(e_o5, e_o6, e_o7)
        electron_count_o += 3
        self.wait(0.5)

        # Then pair the first one
        e_o8 = electron_down.copy().move_to(p2_boxes_o[0].get_center())
        self.play(FadeIn(e_o8, shift=DOWN), run_time=0.3)
        electrons_oxygen.add(e_o8)
        electron_count_o += 1
        self.wait(1)

        # Spectroscopic notation for Oxygen
        oxygen_config_spec = MathTex(r"\text{Spectroscopic: } 1s^2 2s^2 2p^4", color=RED_D, font_size=50).to_edge(DOWN, buff=1.0).shift(LEFT * 3)
        self.play(Write(oxygen_config_spec))
        self.wait(2)

        self.play(FadeOut(orbital_diagram_title, oxygen_atom, atomic_number_o, orbital_diagram_group, electrons_oxygen, oxygen_config_spec))
        self.clear()

        # --- Scene 6: Example 3 - Sodium (Na) ---
        sodium_title = MathTex(r"\text{Example: Sodium (Na)}", color=BLUE_D, font_size=84)
        self.play(Write(sodium_title))
        self.wait(1)

        atomic_number_na = MathTex(r"\text{Atomic Number (Z) = 11}", color=BLACK, font_size=48).next_to(sodium_title, DOWN, buff=1.0)
        self.play(FadeIn(atomic_number_na, shift=UP))
        self.wait(1)

        # Full spectroscopic configuration
        full_config_label = MathTex(r"\text{Full Electronic Configuration:}", color=GREEN_D, font_size=50).to_edge(UL, buff=1.0)
        full_config_na = MathTex(r"1s^2 2s^2 2p^6 3s^1", color=RED_D, font_size=72).next_to(full_config_label, DOWN, buff=0.5).align_to(full_config_label, LEFT)
        self.play(FadeIn(full_config_label, shift=LEFT), Write(full_config_na))
        self.wait(2)

        # Noble gas configuration
        noble_gas_label = MathTex(r"\text{Noble Gas Configuration:}", color=GREEN_D, font_size=50).next_to(full_config_na, DOWN, buff=1.5).align_to(full_config_na, LEFT)
        noble_gas_explanation = MathTex(
            r"\text{The core electrons are represented by the symbol of the preceding noble gas.}",
            r"\\ \text{Neon (Ne) has 10 electrons: } 1s^2 2s^2 2p^6",
            color=BLACK,
            font_size=40
        ).next_to(noble_gas_label, DOWN, buff=0.5).align_to(noble_gas_label, LEFT)
        self.play(FadeIn(noble_gas_label, shift=LEFT), FadeIn(noble_gas_explanation, shift=LEFT))
        self.wait(3)

        noble_gas_config_na = MathTex(r"[\text{Ne}] 3s^1", color=RED_D, font_size=72).next_to(noble_gas_explanation, DOWN, buff=0.5).align_to(noble_gas_explanation, LEFT)
        self.play(Write(noble_gas_config_na))
        self.wait(2)

        self.play(FadeOut(sodium_title, atomic_number_na, full_config_label, full_config_na,
                          noble_gas_label, noble_gas_explanation, noble_gas_config_na))
        self.clear()

        # --- Final Summary / End Screen ---
        summary_title = MathTex(r"\text{Summary of Electronic Configuration}", color=BLUE_D, font_size=96)
        self.play(Write(summary_title))
        self.wait(1)

        summary_points = VGroup(
            MathTex(r"\bullet \text{ Electrons fill orbitals based on energy (Aufbau).}", color=BLACK, font_size=48),
            MathTex(r"\bullet \text{ Max 2 electrons per orbital with opposite spins (Pauli).}", color=BLACK, font_size=48),
            MathTex(r"\bullet \text{ Degenerate orbitals fill singly first (Hund's Rule).}", color=BLACK, font_size=48),
            MathTex(r"\bullet \text{ Notations: Spectroscopic } (1s^2) \text{ and Orbital Diagram } (\uparrow \downarrow).", color=BLACK, font_size=48)
        ).arrange(DOWN, buff=0.8, aligned_edge=LEFT).next_to(summary_title, DOWN, buff=1.0)

        self.play(FadeIn(summary_points, shift=UP, stagger=0.5))
        self.wait(3)

        thank_you = MathTex(r"\text{Thank You for Watching!}", color=GRAY_D, font_size=60).to_edge(DR, buff=0.5)
        self.play(FadeIn(thank_you, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(self.mobjects)) # Clear all remaining mobjects