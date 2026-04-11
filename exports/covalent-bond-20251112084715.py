from manim import *

# Configure global settings for resolution and FPS
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.background_color = WHITE

class GeneratedScene(Scene):
    def construct(self):
        # --- Scene 1: Introduction to Covalent Bonds ---
        self.camera.background_color = WHITE # Ensure white background for this scene

        title = MathTex(r"\textbf{Covalent Bonds}", color=BLACK, font_size=72)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))
        self.wait(1)

        definition_text = MathTex(
            r"\text{A covalent bond is formed by the }",
            r"\textbf{sharing of electron pairs}",
            r"\text{ between atoms.}",
            color=BLACK, font_size=54
        ).next_to(title, DOWN, buff=0.8)
        definition_text[1].set_color(BLUE) # Highlight "sharing of electron pairs"
        self.play(Write(definition_text))
        self.wait(2)

        why_text = MathTex(
            r"\text{Atoms share electrons to achieve a stable electron configuration,}",
            r"\\",
            r"\text{often satisfying the } \textbf{octet rule} \text{ (8 valence electrons).}",
            color=BLACK, font_size=54
        ).next_to(definition_text, DOWN, buff=0.8)
        why_text[2][10:20].set_color(GREEN) # Highlight "octet rule"
        self.play(Write(why_text))
        self.wait(2)

        # Visual representation of sharing
        atom1_nucleus = Circle(radius=0.3, color=RED, fill_opacity=1).shift(LEFT * 3)
        atom1_label = MathTex(r"\text{Atom A}", color=BLACK, font_size=36).next_to(atom1_nucleus, UP)
        atom1_electron1 = Dot(point=atom1_nucleus.get_center() + LEFT * 0.5 + UP * 0.5, radius=0.1, color=YELLOW)
        atom1_electron2 = Dot(point=atom1_nucleus.get_center() + LEFT * 0.5 + DOWN * 0.5, radius=0.1, color=YELLOW)
        atom1 = VGroup(atom1_nucleus, atom1_label, atom1_electron1, atom1_electron2)

        atom2_nucleus = Circle(radius=0.3, color=BLUE, fill_opacity=1).shift(RIGHT * 3)
        atom2_label = MathTex(r"\text{Atom B}", color=BLACK, font_size=36).next_to(atom2_nucleus, UP)
        atom2_electron1 = Dot(point=atom2_nucleus.get_center() + RIGHT * 0.5 + UP * 0.5, radius=0.1, color=YELLOW)
        atom2_electron2 = Dot(point=atom2_nucleus.get_center() + RIGHT * 0.5 + DOWN * 0.5, radius=0.1, color=YELLOW)
        atom2 = VGroup(atom2_nucleus, atom2_label, atom2_electron1, atom2_electron2)

        self.play(FadeIn(atom1, atom2))
        self.wait(1)

        # Animate atoms moving closer
        self.play(
            atom1.animate.shift(RIGHT * 1.5),
            atom2.animate.shift(LEFT * 1.5),
            run_time=1.5
        )
        self.wait(0.5)

        # Animate electrons sharing
        # Create new dots for the shared pair at the bond location
        shared_electron_pair = VGroup(
            Dot(point=ORIGIN + LEFT * 0.2, radius=0.1, color=YELLOW),
            Dot(point=ORIGIN + RIGHT * 0.2, radius=0.1, color=YELLOW)
        )

        self.play(
            Transform(atom1_electron1, shared_electron_pair[0]),
            Transform(atom2_electron2, shared_electron_pair[1]),
            FadeOut(atom1_electron2, atom2_electron1), # Other electrons fade out for simplicity of this general visual
            run_time=1.5
        )
        self.wait(1)

        bond_line = Line(atom1_nucleus.get_center() + RIGHT * 1.5, atom2_nucleus.get_center() + LEFT * 1.5, color=PURPLE, stroke_width=5)
        bond_label = MathTex(r"\text{Shared Electron Pair (Covalent Bond)}", color=PURPLE, font_size=40).next_to(bond_line, DOWN)
        self.play(Create(bond_line), Write(bond_label))
        self.wait(2)

        self.play(
            FadeOut(title, definition_text, why_text, atom1, atom2, shared_electron_pair, bond_line, bond_label)
        )
        self.clear() # Clear screen for next example

        # --- Scene 2: Example 1 - Hydrogen Molecule (H2) ---
        example1_title = MathTex(r"\textbf{Example 1: Hydrogen Molecule (H}_2\textbf{)}", color=BLACK, font_size=64)
        example1_title.to_edge(UP, buff=0.7)
        self.play(Write(example1_title))
        self.wait(1)

        # Hydrogen atom 1
        h1_nucleus = Circle(radius=0.3, color=RED, fill_opacity=1).shift(LEFT * 4)
        h1_label = MathTex(r"\text{H}", color=BLACK, font_size=48).move_to(h1_nucleus.get_center())
        h1_electron = Dot(point=h1_nucleus.get_center() + UP * 0.5, radius=0.15, color=YELLOW)
        h1_atom = VGroup(h1_nucleus, h1_label, h1_electron)
        h1_valence_shell = Circle(radius=1.0, color=GRAY_A, stroke_width=1).move_to(h1_nucleus.get_center())

        # Hydrogen atom 2
        h2_nucleus = Circle(radius=0.3, color=BLUE, fill_opacity=1).shift(RIGHT * 4)
        h2_label = MathTex(r"\text{H}", color=BLACK, font_size=48).move_to(h2_nucleus.get_center())
        h2_electron = Dot(point=h2_nucleus.get_center() + UP * 0.5, radius=0.15, color=YELLOW)
        h2_atom = VGroup(h2_nucleus, h2_label, h2_electron)
        h2_valence_shell = Circle(radius=1.0, color=GRAY_A, stroke_width=1).move_to(h2_nucleus.get_center())

        self.play(FadeIn(h1_atom, h2_atom))
        self.play(Create(h1_valence_shell), Create(h2_valence_shell))
        self.wait(1)

        # Move atoms closer
        self.play(
            h1_atom.animate.shift(RIGHT * 2),
            h1_valence_shell.animate.shift(RIGHT * 2),
            h2_atom.animate.shift(LEFT * 2),
            h2_valence_shell.animate.shift(LEFT * 2),
            run_time=1.5
        )
        self.wait(0.5)

        # Animate electron sharing
        # Create new dots for the shared pair at the bond location
        shared_electron_pair_h2 = VGroup(
            Dot(point=ORIGIN + LEFT * 0.2 + UP * 0.3, radius=0.15, color=YELLOW),
            Dot(point=ORIGIN + RIGHT * 0.2 + UP * 0.3, radius=0.15, color=YELLOW)
        )

        self.play(
            Transform(h1_electron, shared_electron_pair_h2[0]),
            Transform(h2_electron, shared_electron_pair_h2[1]),
            run_time=1.5
        )
        self.wait(1)

        # Show overlapping shells
        overlapping_shells = VGroup(h1_valence_shell, h2_valence_shell)
        self.play(Indicate(overlapping_shells, scale_factor=1.1, color=ORANGE))
        self.wait(1)

        # Form the bond line
        h2_bond = Line(h1_nucleus.get_center() + RIGHT * 2, h2_nucleus.get_center() + LEFT * 2, color=PURPLE, stroke_width=5)
        h2_bond_label = MathTex(r"\text{Single Covalent Bond}", color=PURPLE, font_size=40).next_to(h2_bond, DOWN)
        self.play(Create(h2_bond), Write(h2_bond_label))
        self.wait(2)

        # Show final H2 molecule
        h2_molecule_label = MathTex(r"\text{H}_2", color=BLACK, font_size=48).next_to(h2_bond, UP, buff=0.5)
        self.play(Write(h2_molecule_label))
        self.wait(2)

        self.play(
            FadeOut(example1_title, h1_atom, h2_atom, h1_valence_shell, h2_valence_shell,
                    shared_electron_pair_h2, h2_bond, h2_bond_label, h2_molecule_label)
        )
        self.clear()

        # --- Scene 3: Example 2 - Water Molecule (H2O) ---
        example2_title = MathTex(r"\textbf{Example 2: Water Molecule (H}_2\textbf{O)}", color=BLACK, font_size=64)
        example2_title.to_edge(UP, buff=0.7)
        self.play(Write(example2_title))
        self.wait(1)

        # Oxygen atom
        o_nucleus = Circle(radius=0.4, color=RED, fill_opacity=1)
        o_label = MathTex(r"\text{O}", color=BLACK, font_size=48).move_to(o_nucleus.get_center())
        # 2 lone pairs (4 electrons), 2 unpaired electrons
        o_electrons = VGroup(
            Dot(point=o_nucleus.get_center() + LEFT * 0.7 + UP * 0.7, radius=0.15, color=YELLOW), # Lone pair 1 (e1)
            Dot(point=o_nucleus.get_center() + LEFT * 0.7 + UP * 0.5, radius=0.15, color=YELLOW), # Lone pair 1 (e2)
            Dot(point=o_nucleus.get_center() + RIGHT * 0.7 + UP * 0.7, radius=0.15, color=YELLOW), # Lone pair 2 (e1)
            Dot(point=o_nucleus.get_center() + RIGHT * 0.7 + UP * 0.5, radius=0.15, color=YELLOW), # Lone pair 2 (e2)
            Dot(point=o_nucleus.get_center() + LEFT * 0.7 + DOWN * 0.7, radius=0.15, color=YELLOW), # Unpaired 1 (e1)
            Dot(point=o_nucleus.get_center() + RIGHT * 0.7 + DOWN * 0.7, radius=0.15, color=YELLOW)  # Unpaired 2 (e2)
        )
        o_atom = VGroup(o_nucleus, o_label, o_electrons).shift(UP * 1.5)
        o_valence_shell = Circle(radius=1.5, color=GRAY_A, stroke_width=1).move_to(o_atom.get_center())

        # Hydrogen atom 1
        h1_nucleus_o = Circle(radius=0.3, color=BLUE, fill_opacity=1).shift(LEFT * 3 + DOWN * 2)
        h1_label_o = MathTex(r"\text{H}", color=BLACK, font_size=48).move_to(h1_nucleus_o.get_center())
        h1_electron_o = Dot(point=h1_nucleus_o.get_center() + UP * 0.5, radius=0.15, color=YELLOW)
        h1_atom_o = VGroup(h1_nucleus_o, h1_label_o, h1_electron_o)
        h1_valence_shell_o = Circle(radius=1.0, color=GRAY_A, stroke_width=1).move_to(h1_atom_o.get_center())

        # Hydrogen atom 2
        h2_nucleus_o = Circle(radius=0.3, color=BLUE, fill_opacity=1).shift(RIGHT * 3 + DOWN * 2)
        h2_label_o = MathTex(r"\text{H}", color=BLACK, font_size=48).move_to(h2_nucleus_o.get_center())
        h2_electron_o = Dot(point=h2_nucleus_o.get_center() + UP * 0.5, radius=0.15, color=YELLOW)
        h2_atom_o = VGroup(h2_nucleus_o, h2_label_o, h2_electron_o)
        h2_valence_shell_o = Circle(radius=1.0, color=GRAY_A, stroke_width=1).move_to(h2_atom_o.get_center())

        self.play(FadeIn(o_atom, h1_atom_o, h2_atom_o))
        self.play(Create(o_valence_shell), Create(h1_valence_shell_o), Create(h2_valence_shell_o))
        self.wait(1)

        # Move H atoms to bond with O
        self.play(
            h1_atom_o.animate.move_to(o_atom.get_center() + LEFT * 1.5 + DOWN * 1.5),
            h1_valence_shell_o.animate.move_to(o_atom.get_center() + LEFT * 1.5 + DOWN * 1.5),
            h2_atom_o.animate.move_to(o_atom.get_center() + RIGHT * 1.5 + DOWN * 1.5),
            h2_valence_shell_o.animate.move_to(o_atom.get_center() + RIGHT * 1.5 + DOWN * 1.5),
            run_time=2
        )
        self.wait(0.5)

        # Animate electron sharing for H2O
        # Shared pairs positions
        shared_pair1_pos = o_atom.get_center() + LEFT * 0.8 + DOWN * 0.8
        shared_pair2_pos = o_atom.get_center() + RIGHT * 0.8 + DOWN * 0.8

        shared_electron_pair_h2o_1 = VGroup(
            Dot(point=shared_pair1_pos + LEFT * 0.1, radius=0.15, color=YELLOW),
            Dot(point=shared_pair1_pos + RIGHT * 0.1, radius=0.15, color=YELLOW)
        )
        shared_electron_pair_h2o_2 = VGroup(
            Dot(point=shared_pair2_pos + LEFT * 0.1, radius=0.15, color=YELLOW),
            Dot(point=shared_pair2_pos + RIGHT * 0.1, radius=0.15, color=YELLOW)
        )

        self.play(
            Transform(o_electrons[4], shared_electron_pair_h2o_1[0]), # O's unpaired electron 1
            Transform(h1_electron_o, shared_electron_pair_h2o_1[1]), # H1's electron
            Transform(o_electrons[5], shared_electron_pair_h2o_2[0]), # O's unpaired electron 2
            Transform(h2_electron_o, shared_electron_pair_h2o_2[1]), # H2's electron
            run_time=1.5
        )
        self.wait(1)

        # Show bonds
        bond_h1_o = Line(o_atom.get_center() + LEFT * 0.5 + DOWN * 0.5, h1_atom_o.get_center() + UP * 0.5 + RIGHT * 0.5, color=PURPLE, stroke_width=5)
        bond_h2_o = Line(o_atom.get_center() + RIGHT * 0.5 + DOWN * 0.5, h2_atom_o.get_center() + UP * 0.5 + LEFT * 0.5, color=PURPLE, stroke_width=5)
        self.play(Create(bond_h1_o), Create(bond_h2_o))
        self.wait(1)

        # Label lone pairs
        lone_pair_label1 = MathTex(r"\text{Lone Pair}", color=ORANGE, font_size=36).next_to(o_electrons[0], LEFT, buff=0.2)
        lone_pair_label2 = MathTex(r"\text{Lone Pair}", color=ORANGE, font_size=36).next_to(o_electrons[2], RIGHT, buff=0.2)
        self.play(Write(lone_pair_label1), Write(lone_pair_label2))
        self.wait(1)

        # Show final H2O molecule structure
        h2o_molecule_label = MathTex(r"\text{H}_2\text{O}", color=BLACK, font_size=48).next_to(o_atom, UP, buff=0.5)
        self.play(Write(h2o_molecule_label))
        self.wait(2)

        self.play(
            FadeOut(example2_title, o_atom, h1_atom_o, h2_atom_o, o_valence_shell, h1_valence_shell_o, h2_valence_shell_o,
                    shared_electron_pair_h2o_1, shared_electron_pair_h2o_2, bond_h1_o, bond_h2_o,
                    lone_pair_label1, lone_pair_label2, h2o_molecule_label)
        )
        self.clear()

        # --- Scene 4: Example 3 - Carbon Dioxide Molecule (CO2) ---
        example3_title = MathTex(r"\textbf{Example 3: Carbon Dioxide Molecule (CO}_2\textbf{)}", color=BLACK, font_size=64)
        example3_title.to_edge(UP, buff=0.7)
        self.play(Write(example3_title))
        self.wait(1)

        # Carbon atom
        c_nucleus = Circle(radius=0.4, color=GREEN, fill_opacity=1)
        c_label = MathTex(r"\text{C}", color=BLACK, font_size=48).move_to(c_nucleus.get_center())
        # 4 unpaired electrons
        c_electrons = VGroup(
            Dot(point=c_nucleus.get_center() + UP * 0.7, radius=0.15, color=YELLOW),    # C_e_up (index 0)
            Dot(point=c_nucleus.get_center() + DOWN * 0.7, radius=0.15, color=YELLOW),  # C_e_down (index 1)
            Dot(point=c_nucleus.get_center() + LEFT * 0.7, radius=0.15, color=YELLOW),  # C_e_left (index 2)
            Dot(point=c_nucleus.get_center() + RIGHT * 0.7, radius=0.15, color=YELLOW) # C_e_right (index 3)
        )
        c_atom = VGroup(c_nucleus, c_label, c_electrons)
        c_valence_shell = Circle(radius=1.5, color=GRAY_A, stroke_width=1).move_to(c_atom.get_center())

        # Oxygen atom 1
        o1_nucleus_co2 = Circle(radius=0.4, color=RED, fill_opacity=1).shift(LEFT * 4)
        o1_label_co2 = MathTex(r"\text{O}", color=BLACK, font_size=48).move_to(o1_nucleus_co2.get_center())
        # 2 lone pairs (4 electrons), 2 unpaired electrons
        o1_electrons_co2 = VGroup(
            Dot(point=o1_nucleus_co2.get_center() + UP * 0.7 + LEFT * 0.7, radius=0.15, color=YELLOW), # LP1_e1 (0)
            Dot(point=o1_nucleus_co2.get_center() + UP * 0.7 + LEFT * 0.5, radius=0.15, color=YELLOW), # LP1_e2 (1)
            Dot(point=o1_nucleus_co2.get_center() + DOWN * 0.7 + LEFT * 0.7, radius=0.15, color=YELLOW), # LP2_e1 (2)
            Dot(point=o1_nucleus_co2.get_center() + DOWN * 0.7 + LEFT * 0.5, radius=0.15, color=YELLOW), # LP2_e2 (3)
            Dot(point=o1_nucleus_co2.get_center() + UP * 0.7 + RIGHT * 0.7, radius=0.15, color=YELLOW), # Unpaired 1 (4)
            Dot(point=o1_nucleus_co2.get_center() + DOWN * 0.7 + RIGHT * 0.7, radius=0.15, color=YELLOW)  # Unpaired 2 (5)
        )
        o1_atom_co2 = VGroup(o1_nucleus_co2, o1_label_co2, o1_electrons_co2)
        o1_valence_shell_co2 = Circle(radius=1.5, color=GRAY_A, stroke_width=1).move_to(o1_atom_co2.get_center())

        # Oxygen atom 2
        o2_nucleus_co2 = Circle(radius=0.4, color=RED, fill_opacity=1).shift(RIGHT * 4)
        o2_label_co2 = MathTex(r"\text{O}", color=BLACK, font_size=48).move_to(o2_nucleus_co2.get_center())
        # 2 lone pairs (4 electrons), 2 unpaired electrons
        o2_electrons_co2 = VGroup(
            Dot(point=o2_nucleus_co2.get_center() + UP * 0.7 + RIGHT * 0.7, radius=0.15, color=YELLOW), # LP1_e1 (0)
            Dot(point=o2_nucleus_co2.get_center() + UP * 0.7 + RIGHT * 0.5, radius=0.15, color=YELLOW), # LP1_e2 (1)
            Dot(point=o2_nucleus_co2.get_center() + DOWN * 0.7 + RIGHT * 0.7, radius=0.15, color=YELLOW), # LP2_e1 (2)
            Dot(point=o2_nucleus_co2.get_center() + DOWN * 0.7 + RIGHT * 0.5, radius=0.15, color=YELLOW), # LP2_e2 (3)
            Dot(point=o2_nucleus_co2.get_center() + UP * 0.7 + LEFT * 0.7, radius=0.15, color=YELLOW), # Unpaired 1 (4)
            Dot(point=o2_nucleus_co2.get_center() + DOWN * 0.7 + LEFT * 0.7, radius=0.15, color=YELLOW)  # Unpaired 2 (5)
        )
        o2_atom_co2 = VGroup(o2_nucleus_co2, o2_label_co2, o2_electrons_co2)
        o2_valence_shell_co2 = Circle(radius=1.5, color=GRAY_A, stroke_width=1).move_to(o2_atom_co2.get_center())

        self.play(FadeIn(c_atom, o1_atom_co2, o2_atom_co2))
        self.play(Create(c_valence_shell), Create(o1_valence_shell_co2), Create(o2_valence_shell_co2))
        self.wait(1)

        # Move O atoms to bond with C
        self.play(
            o1_atom_co2.animate.shift(RIGHT * 2),
            o1_valence_shell_co2.animate.shift(RIGHT * 2),
            o2_atom_co2.animate.shift(LEFT * 2),
            o2_valence_shell_co2.animate.shift(LEFT * 2),
            run_time=2
        )
        self.wait(0.5)

        # Animate electron sharing for CO2 (double bonds)
        # Shared pair positions for C-O1 bond
        shared_co1_pair1_pos = c_atom.get_center() + LEFT * 0.8 + UP * 0.3
        shared_co1_pair2_pos = c_atom.get_center() + LEFT * 0.8 + DOWN * 0.3

        # Shared pair positions for C-O2 bond
        shared_co2_pair1_pos = c_atom.get_center() + RIGHT * 0.8 + UP * 0.3
        shared_co2_pair2_pos = c_atom.get_center() + RIGHT * 0.8 + DOWN * 0.3

        shared_electron_co1_1 = VGroup(
            Dot(point=shared_co1_pair1_pos + LEFT * 0.1, radius=0.15, color=YELLOW),
            Dot(point=shared_co1_pair1_pos + RIGHT * 0.1, radius=0.15, color=YELLOW)
        )
        shared_electron_co1_2 = VGroup(
            Dot(point=shared_co1_pair2_pos + LEFT * 0.1, radius=0.15, color=YELLOW),
            Dot(point=shared_co1_pair2_pos + RIGHT * 0.1, radius=0.15, color=YELLOW)
        )
        shared_electron_co2_1 = VGroup(
            Dot(point=shared_co2_pair1_pos + LEFT * 0.1, radius=0.15, color=YELLOW),
            Dot(point=shared_co2_pair1_pos + RIGHT * 0.1, radius=0.15, color=YELLOW)
        )
        shared_electron_co2_2 = VGroup(
            Dot(point=shared_co2_pair2_pos + LEFT * 0.1, radius=0.15, color=YELLOW),
            Dot(point=shared_co2_pair2_pos + RIGHT * 0.1, radius=0.15, color=YELLOW)
        )

        # First double bond (C-O1)
        self.play(
            Transform(c_electrons[2], shared_electron_co1_1[0]), # C's left electron
            Transform(o1_electrons_co2[4], shared_electron_co1_1[1]), # O1's unpaired electron 1
            Transform(c_electrons[0], shared_electron_co1_2[0]), # C's up electron
            Transform(o1_electrons_co2[5], shared_electron_co1_2[1]), # O1's unpaired electron 2
            run_time=1.5
        )
        self.wait(0.5)

        # Second double bond (C-O2)
        self.play(
            Transform(c_electrons[3], shared_electron_co2_1[0]), # C's right electron
            Transform(o2_electrons_co2[4], shared_electron_co2_1[1]), # O2's unpaired electron 1
            Transform(c_electrons[1], shared_electron_co2_2[0]), # C's down electron
            Transform(o2_electrons_co2[5], shared_electron_co2_2[1]), # O2's unpaired electron 2
            run_time=1.5
        )
        self.wait(1)

        # Show double bonds as lines
        bond_co1_1 = Line(c_atom.get_center() + LEFT * 0.5 + UP * 0.2, o1_atom_co2.get_center() + RIGHT * 0.5 + UP * 0.2, color=PURPLE, stroke_width=5)
        bond_co1_2 = Line(c_atom.get_center() + LEFT * 0.5 + DOWN * 0.2, o1_atom_co2.get_center() + RIGHT * 0.5 + DOWN * 0.2, color=PURPLE, stroke_width=5)
        bond_co2_1 = Line(c_atom.get_center() + RIGHT * 0.5 + UP * 0.2, o2_atom_co2.get_center() + LEFT * 0.5 + UP * 0.2, color=PURPLE, stroke_width=5)
        bond_co2_2 = Line(c_atom.get_center() + RIGHT * 0.5 + DOWN * 0.2, o2_atom_co2.get_center() + LEFT * 0.5 + DOWN * 0.2, color=PURPLE, stroke_width=5)

        self.play(Create(bond_co1_1), Create(bond_co1_2), Create(bond_co2_1), Create(bond_co2_2))
        self.wait(1)

        # Label lone pairs on Oxygen atoms
        o1_lone_pair_label1 = MathTex(r"\text{Lone Pair}", color=ORANGE, font_size=36).next_to(o1_electrons_co2[0], UP, buff=0.2)
        o1_lone_pair_label2 = MathTex(r"\text{Lone Pair}", color=ORANGE, font_size=36).next_to(o1_electrons_co2[2], DOWN, buff=0.2)
        o2_lone_pair_label1 = MathTex(r"\text{Lone Pair}", color=ORANGE, font_size=36).next_to(o2_electrons_co2[0], UP, buff=0.2)
        o2_lone_pair_label2 = MathTex(r"\text{Lone Pair}", color=ORANGE, font_size=36).next_to(o2_electrons_co2[2], DOWN, buff=0.2)
        self.play(Write(o1_lone_pair_label1), Write(o1_lone_pair_label2),
                  Write(o2_lone_pair_label1), Write(o2_lone_pair_label2))
        self.wait(1)

        # Show final CO2 molecule structure
        co2_molecule_label = MathTex(r"\text{CO}_2", color=BLACK, font_size=48).next_to(c_atom, UP, buff=0.5)
        self.play(Write(co2_molecule_label))
        self.wait(2)

        self.play(
            FadeOut(example3_title, c_atom, o1_atom_co2, o2_atom_co2, c_valence_shell, o1_valence_shell_co2, o2_valence_shell_co2,
                    shared_electron_co1_1, shared_electron_co1_2, shared_electron_co2_1, shared_electron_co2_2,
                    bond_co1_1, bond_co1_2, bond_co2_1, bond_co2_2,
                    o1_lone_pair_label1, o1_lone_pair_label2, o2_lone_pair_label1, o2_lone_pair_label2,
                    co2_molecule_label)
        )
        self.clear()
