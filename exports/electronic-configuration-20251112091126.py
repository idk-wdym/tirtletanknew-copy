from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Configure resolution and background
        self.camera.background_color = WHITE
        config.pixel_width = 1920
        config.pixel_height = 1080
        config.frame_rate = 30

        # --- Scene 1: Introduction ---
        self.introduction_to_electronic_configuration()
        self.clear()

        # --- Scene 2: Key Principles ---
        self.key_principles()
        self.clear()

        # --- Scene 3: Orbital Types and Capacities ---
        self.orbital_types_and_capacities()
        self.clear()

        # --- Scene 4: Example 1 - Hydrogen ---
        self.example_hydrogen()
        self.clear()

        # --- Scene 5: Example 2 - Carbon ---
        self.example_carbon()
        self.clear()

        # --- Scene 6: Example 3 - Oxygen ---
        self.example_oxygen()
        self.clear()

    def introduction_to_electronic_configuration(self):
        title = MathTex(
            "\\text{Electronic Configuration}",
            color=BLUE_D,
            font_size=80
        ).to_edge(UP, buff=0.7)

        definition = MathTex(
            "\\text{The arrangement of electrons in atomic orbitals.}",
            color=BLACK,
            font_size=50
        ).next_to(title, DOWN, buff=1)

        key_concepts_title = MathTex(
            "\\text{Key Concepts:}",
            color=BLACK,
            font_size=40
        ).next_to(definition, DOWN, buff=1.0).align_to(definition, LEFT)

        concept1 = MathTex(
            "\\bullet \\text{ Energy Levels (Shells)}",
            color=BLACK,
            font_size=35
        ).next_to(key_concepts_title, DOWN, buff=0.5).align_to(key_concepts_title, LEFT)

        concept2 = MathTex(
            "\\bullet \\text{ Subshells (s, p, d, f)}",
            color=BLACK,
            font_size=35
        ).next_to(concept1, DOWN, buff=0.3).align_to(concept1, LEFT)

        concept3 = MathTex(
            "\\bullet \\text{ Orbitals (Regions of probability for electrons)}",
            color=BLACK,
            font_size=35
        ).next_to(concept2, DOWN, buff=0.3).align_to(concept2, LEFT)

        self.play(
            Write(title)
        )
        self.wait(1)
        self.play(
            FadeIn(definition, shift=UP)
        )
        self.wait(1.5)
        self.play(
            Write(key_concepts_title)
        )
        self.play(
            FadeIn(concept1, shift=LEFT)
        )
        self.play(
            FadeIn(concept2, shift=LEFT)
        )
        self.play(
            FadeIn(concept3, shift=LEFT)
        )
        self.wait(2)

    def key_principles(self):
        title = MathTex(
            "\\text{Key Principles for Filling Orbitals}",
            color=BLUE_D,
            font_size=70
        ).to_edge(UP, buff=0.7)

        self.play(Write(title))
        self.wait(1)

        # Aufbau Principle
        aufbau_title = MathTex(
            "1. \\text{ Aufbau Principle}",
            color=RED_D,
            font_size=50
        ).to_edge(LEFT, buff=1).shift(UP*1.5)

        aufbau_text = VGroup(
            MathTex("\\text{Electrons fill atomic orbitals of the lowest available}", color=BLACK, font_size=35),
            MathTex("\\text{energy levels before occupying higher levels.}", color=BLACK, font_size=35)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(aufbau_title, DOWN, buff=0.5).align_to(aufbau_title, LEFT)

        # Orbital energy diagram (simplified for demonstration)
        orbital_1s = Rectangle(width=1, height=0.6, color=BLACK).set_stroke(width=2).shift(LEFT*4 + DOWN*1.5)
        label_1s = MathTex("1s", color=BLACK, font_size=30).next_to(orbital_1s, DOWN, buff=0.2)

        orbital_2s = Rectangle(width=1, height=0.6, color=BLACK).set_stroke(width=2).shift(LEFT*2 + DOWN*0.5)
        label_2s = MathTex("2s", color=BLACK, font_size=30).next_to(orbital_2s, DOWN, buff=0.2)

        orbital_2p_group = VGroup(*[
            Rectangle(width=1, height=0.6, color=BLACK).set_stroke(width=2)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.2).shift(RIGHT*2 + UP*0.5)
        label_2p = MathTex("2p", color=BLACK, font_size=30).next_to(orbital_2p_group, DOWN, buff=0.2)

        electron_up = MathTex("\\uparrow", color=BLUE, font_size=40)
        electron_down = MathTex("\\downarrow", color=BLUE, font_size=40)

        self.play(Write(aufbau_title))
        self.play(FadeIn(aufbau_text, shift=UP))
        self.wait(1)
        self.play(
            Create(orbital_1s), Write(label_1s),
            Create(orbital_2s), Write(label_2s),
            Create(orbital_2p_group), Write(label_2p)
        )
        self.wait(0.5)
        self.play(FadeIn(electron_up.copy().move_to(orbital_1s.get_center()), scale=0.5))
        self.play(FadeIn(electron_down.copy().move_to(orbital_1s.get_center()), scale=0.5))
        self.play(FadeIn(electron_up.copy().move_to(orbital_2s.get_center()), scale=0.5))
        self.play(FadeIn(electron_down.copy().move_to(orbital_2s.get_center()), scale=0.5))
        self.play(FadeIn(electron_up.copy().move_to(orbital_2p_group[0].get_center()), scale=0.5))
        self.wait(1)
        self.play(FadeOut(VGroup(orbital_1s, label_1s, orbital_2s, label_2s, orbital_2p_group, label_2p, aufbau_title, aufbau_text, *self.mobjects[len(self.mobjects)-5:]))) # Fade out electrons and previous elements


        # Pauli Exclusion Principle
        pauli_title = MathTex(
            "2. \\text{ Pauli Exclusion Principle}",
            color=RED_D,
            font_size=50
        ).to_edge(LEFT, buff=1).shift(UP*1.5)

        pauli_text_wrapped = VGroup(
            MathTex("\\text{No two electrons in the same atom can have identical quantum numbers.}", color=BLACK, font_size=35),
            MathTex("\\text{An orbital can hold a maximum of two electrons,}", color=BLACK, font_size=35),
            MathTex("\\text{which must have opposite spins.}", color=BLACK, font_size=35)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(pauli_title, DOWN, buff=0.5).align_to(pauli_title, LEFT)


        orbital_example = Rectangle(width=1.5, height=0.8, color=BLACK).set_stroke(width=2).shift(RIGHT*3)
        electron_up_m = MathTex("\\uparrow", color=BLUE, font_size=50).move_to(orbital_example.get_center() + LEFT*0.2)
        electron_down_m = MathTex("\\downarrow", color=BLUE, font_size=50).move_to(orbital_example.get_center() + RIGHT*0.2)
        electron_up_bad = MathTex("\\uparrow", color=RED, font_size=50).move_to(orbital_example.get_center() + RIGHT*0.2)

        self.play(Write(pauli_title))
        self.play(FadeIn(pauli_text_wrapped, shift=UP))
        self.wait(1)
        self.play(Create(orbital_example))
        self.play(FadeIn(electron_up_m, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(electron_down_m, shift=DOWN))
        self.wait(1)
        self.play(
            FadeOut(electron_down_m),
            FadeIn(electron_up_bad)
        )
        self.play(Indicate(electron_up_bad, color=RED, scale_factor=1.5))
        self.wait(0.5)
        self.play(
            FadeOut(electron_up_bad),
            FadeIn(electron_down_m)
        )
        self.wait(1)
        self.play(FadeOut(VGroup(orbital_example, electron_up_m, electron_down_m, pauli_title, pauli_text_wrapped)))


        # Hund's Rule
        hund_title = MathTex(
            "3. \\text{ Hund's Rule}",
            color=RED_D,
            font_size=50
        ).to_edge(LEFT, buff=1).shift(UP*1.5)

        hund_text_wrapped = VGroup(
            MathTex("\\text{When filling degenerate orbitals (orbitals of equal energy),}", color=BLACK, font_size=35),
            MathTex("\\text{electrons fill each orbital singly before any orbital is doubly occupied.}", color=BLACK, font_size=35),
            MathTex("\\text{All singly occupied orbitals must have parallel spins.}", color=BLACK, font_size=35)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(hund_title, DOWN, buff=0.5).align_to(hund_title, LEFT)


        p_orbitals = VGroup(*[
            Rectangle(width=1, height=0.6, color=BLACK).set_stroke(width=2)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.2).shift(RIGHT*3)

        electron_h1 = MathTex("\\uparrow", color=BLUE, font_size=40).move_to(p_orbitals[0].get_center())
        electron_h2 = MathTex("\\uparrow", color=BLUE, font_size=40).move_to(p_orbitals[1].get_center())
        electron_h3 = MathTex("\\uparrow", color=BLUE, font_size=40).move_to(p_orbitals[2].get_center())
        electron_h4_bad = MathTex("\\downarrow", color=RED, font_size=40).move_to(p_orbitals[1].get_center())
        electron_h4_good = MathTex("\\downarrow", color=BLUE, font_size=40).move_to(p_orbitals[0].get_center())

        self.play(Write(hund_title))
        self.play(FadeIn(hund_text_wrapped, shift=UP))
        self.wait(1)
        self.play(Create(p_orbitals))
        self.wait(0.5)
        self.play(FadeIn(electron_h1, shift=UP))
        self.play(FadeIn(electron_h2, shift=UP))
        self.play(FadeIn(electron_h3, shift=UP))
        self.wait(1)
        # Demonstrate incorrect filling
        self.play(FadeIn(electron_h4_bad, shift=DOWN))
        self.play(Indicate(electron_h4_bad, color=RED, scale_factor=1.5))
        self.wait(0.5)
        self.play(FadeOut(electron_h4_bad))
        # Demonstrate correct filling
        self.play(FadeIn(electron_h4_good, shift=DOWN))
        self.wait(1)
        self.play(FadeOut(VGroup(p_orbitals, electron_h1, electron_h2, electron_h3, electron_h4_good, hund_title, hund_text_wrapped)))
        self.wait(1)

    def orbital_types_and_capacities(self):
        title = MathTex(
            "\\text{Orbital Types and Capacities}",
            color=BLUE_D,
            font_size=70
        ).to_edge(UP, buff=0.7)

        self.play(Write(title))
        self.wait(1)

        # S-orbital
        s_orbital_label = MathTex("\\text{s-orbital}", color=BLACK, font_size=45).shift(UP*2.5 + LEFT*5)
        s_shape = Sphere(radius=0.8, color=YELLOW_B, opacity=0.7).shift(LEFT*5)
        s_capacity = MathTex("\\text{Capacity: 2 electrons}", color=BLACK, font_size=35).next_to(s_shape, DOWN, buff=0.5)

        self.play(Write(s_orbital_label))
        self.play(Create(s_shape))
        self.play(Write(s_capacity))
        self.wait(1.5)

        # P-orbitals
        p_orbital_label = MathTex("\\text{p-orbitals}", color=BLACK, font_size=45).shift(UP*2.5 + RIGHT*0.5)
        
        # Simpler 2D representation for p-orbitals (dumbbell shapes)
        p_shape_x = VGroup(
            Ellipse(width=1.5, height=0.8, color=GREEN_D, fill_opacity=0.7).shift(LEFT*0.75),
            Ellipse(width=1.5, height=0.8, color=GREEN_D, fill_opacity=0.7).shift(RIGHT*0.75)
        ).arrange(RIGHT, buff=0.01).rotate(PI/2) # Vertical dumbbell
        p_shape_y = VGroup(
            Ellipse(width=1.5, height=0.8, color=GREEN_D, fill_opacity=0.7).shift(LEFT*0.75),
            Ellipse(width=1.5, height=0.8, color=GREEN_D, fill_opacity=0.7).shift(RIGHT*0.75)
        ).arrange(RIGHT, buff=0.01) # Horizontal dumbbell

        p_shapes = VGroup(p_shape_x, p_shape_y).arrange(RIGHT, buff=1.5).shift(RIGHT*0.5)
        p_capacity = MathTex("\\text{Capacity: 6 electrons (3 orbitals)}", color=BLACK, font_size=35).next_to(p_shapes, DOWN, buff=0.5)

        self.play(Write(p_orbital_label))
        self.play(Create(p_shapes[0]))
        self.play(Create(p_shapes[1]))
        self.play(Write(p_capacity))
        self.wait(1.5)

        # D-orbitals (brief mention)
        d_orbital_label = MathTex("\\text{d-orbitals}", color=BLACK, font_size=45).shift(UP*2.5 + RIGHT*6)
        d_text = MathTex("\\text{More complex shapes (5 orbitals)}", color=BLACK, font_size=35).next_to(d_orbital_label, DOWN, buff=0.5)
        d_capacity = MathTex("\\text{Capacity: 10 electrons}", color=BLACK, font_size=35).next_to(d_text, DOWN, buff=0.3)

        self.play(Write(d_orbital_label))
        self.play(Write(d_text))
        self.play(Write(d_capacity))
        self.wait(2)

        self.play(
            FadeOut(s_orbital_label, s_shape, s_capacity),
            FadeOut(p_orbital_label, p_shapes, p_capacity),
            FadeOut(d_orbital_label, d_text, d_capacity)
        )

        # Energy level diagram
        energy_diagram_title = MathTex("\\text{Orbital Filling Order (Simplified)}", color=BLUE_D, font_size=50).to_edge(UP, buff=0.7)
        self.play(Write(energy_diagram_title))

        # Create the energy level diagram
        levels = VGroup(
            MathTex("1s", color=BLACK, font_size=40).shift(LEFT*4 + DOWN*2.5),
            MathTex("2s", color=BLACK, font_size=40).shift(LEFT*4 + DOWN*1.5),
            MathTex("2p", color=BLACK, font_size=40).shift(LEFT*2 + DOWN*0.5),
            MathTex("3s", color=BLACK, font_size=40).shift(LEFT*4 + DOWN*0.5),
            MathTex("3p", color=BLACK, font_size=40).shift(LEFT*2 + UP*0.5),
            MathTex("4s", color=BLACK, font_size=40).shift(LEFT*4 + UP*0.5),
            MathTex("3d", color=BLACK, font_size=40).shift(RIGHT*0 + UP*1.5),
            MathTex("4p", color=BLACK, font_size=40).shift(LEFT*2 + UP*1.5),
        )

        # Define points for arrows in the correct filling order
        points_order = [
            levels[0].get_center(), # 1s
            levels[1].get_center(), # 2s
            levels[2].get_center(), # 2p
            levels[3].get_center(), # 3s
            levels[4].get_center(), # 3p
            levels[5].get_center(), # 4s
            levels[6].get_center(), # 3d
            levels[7].get_center(), # 4p
        ]

        arrows = VGroup()
        for i in range(len(points_order) - 1):
            arrow = Arrow(points_order[i], points_order[i+1], buff=0.1, color=PURPLE_D, stroke_width=4, tip_length=0.2)
            arrows.add(arrow)

        self.play(FadeIn(levels, shift=UP))
        self.wait(1)
        self.play(Create(arrows), run_time=3)
        self.wait(2)
        self.play(FadeOut(VGroup(energy_diagram_title, levels, arrows)))


    def create_orbital_diagram(self, config_str, num_electrons, title_text, config_label_pos=DOWN*3.5):
        # Parse configuration string to determine orbitals needed
        orbitals_data = []
        current_level = ""
        current_type = ""
        for char in config_str:
            if char.isdigit():
                if current_level and current_type:
                    orbitals_data.append((int(current_level), current_type))
                current_level = char
                current_type = ""
            elif char.isalpha():
                current_type += char
            else: # For spaces or other separators
                if current_level and current_type:
                    orbitals_data.append((int(current_level), current_type))
                current_level = ""
                current_type = ""
        if current_level and current_type:
            orbitals_data.append((int(current_level), current_type))

        # Remove duplicates and sort by energy level (simplified)
        unique_orbitals_keys = []
        seen = set()
        for level, o_type in orbitals_data:
            key = (level, o_type)
            if key not in seen:
                unique_orbitals_keys.append(key)
                seen.add(key)

        # Sort based on a simplified energy order (1s, 2s, 2p, 3s, 3p, 4s, 3d, ...)
        orbital_order_priority = {"s": 0, "p": 1, "d": 2, "f": 3}
        unique_orbitals_keys.sort(key=lambda x: (x[0], orbital_order_priority.get(x[1], 99)))

        orbital_mobject_groups = VGroup() # Each element will be a VGroup of boxes for 1s, 2s, 2p etc.
        orbital_label_mobjects = VGroup() # Labels for each of these groups

        for level, o_type in unique_orbitals_keys:
            num_boxes = 1 if o_type == 's' else (3 if o_type == 'p' else (5 if o_type == 'd' else 7))
            
            boxes_for_type = VGroup()
            for _ in range(num_boxes):
                box = Rectangle(width=1, height=0.6, color=BLACK).set_stroke(width=2)
                boxes_for_type.add(box)
            boxes_for_type.arrange(RIGHT, buff=0.2)
            
            label = MathTex(f"{level}{o_type}", color=BLACK, font_size=35).next_to(boxes_for_type, DOWN, buff=0.2)
            
            orbital_mobject_groups.add(boxes_for_type)
            orbital_label_mobjects.add(label)

        # Arrange the entire set of orbital groups and labels
        orbital_mobject_groups.arrange(RIGHT, buff=1.0).center().shift(UP*1.5)
        
        # Position labels relative to their respective orbital groups
        for i, group in enumerate(orbital_mobject_groups):
            orbital_label_mobjects[i].next_to(group, DOWN, buff=0.2)

        # Title and atomic number
        main_title = MathTex(title_text, color=BLUE_D, font_size=70).to_edge(UP, buff=0.7)
        atomic_number_label = MathTex(f"\\text{{Atomic Number (Z)}} = {num_electrons}", color=BLACK, font_size=45).next_to(main_title, DOWN, buff=0.5)
        
        self.play(Write(main_title))
        self.play(FadeIn(atomic_number_label, shift=UP))
        self.wait(0.5)
        self.play(Create(orbital_mobject_groups), Write(orbital_label_mobjects))
        self.wait(1)

        # Fill electrons according to Aufbau, Hund's, and Pauli principles
        electrons_filled = 0
        electron_mobjects = []

        for i, (level, o_type) in enumerate(unique_orbitals_keys):
            num_boxes = 1 if o_type == 's' else (3 if o_type == 'p' else (5 if o_type == 'd' else 7))
            current_orbital_group = orbital_mobject_groups[i]

            # First pass: Fill each orbital singly with up-spin (Hund's Rule)
            for j in range(num_boxes):
                if electrons_filled < num_electrons:
                    electron = MathTex("\\uparrow", color=BLUE, font_size=40).move_to(current_orbital_group[j].get_center())
                    self.play(FadeIn(electron, shift=UP*0.5), run_time=0.3)
                    electron_mobjects.append(electron)
                    electrons_filled += 1
                else:
                    break
            if electrons_filled == num_electrons:
                break
            self.wait(0.2)

            # Second pass: Pair up electrons with down-spin (Pauli Exclusion Principle)
            for j in range(num_boxes):
                if electrons_filled < num_electrons:
                    # Only add a down-spin if an up-spin is already present in this box
                    # (This is implicitly handled by the order of loops, as up-spins are filled first)
                    electron = MathTex("\\downarrow", color=BLUE, font_size=40).move_to(current_orbital_group[j].get_center())
                    self.play(FadeIn(electron, shift=DOWN*0.5), run_time=0.3)
                    electron_mobjects.append(electron)
                    electrons_filled += 1
                else:
                    break
            if electrons_filled == num_electrons:
                break
            self.wait(0.2)

        final_config_label = MathTex(
            f"\\text{{Electronic Configuration: }} {config_str}",
            color=GREEN_D,
            font_size=50
        ).shift(config_label_pos)

        self.play(Write(final_config_label))
        self.wait(2)

        self.play(
            FadeOut(main_title, atomic_number_label, orbital_mobject_groups, orbital_label_mobjects, final_config_label, *electron_mobjects)
        )


    def example_hydrogen(self):
        self.create_orbital_diagram("1s^1", 1, "\\text{Example 1: Hydrogen (H)}")

    def example_carbon(self):
        self.create_orbital_diagram("1s^2 2s^2 2p^2", 6, "\\text{Example 2: Carbon (C)}")

    def example_oxygen(self):
        self.create_orbital_diagram("1s^2 2s^2 2p^4", 8, "\\text{Example 3: Oxygen (O)}")