from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # --- Scene Configuration ---
        # Set the camera frame to 16:9 aspect ratio, suitable for 1920x1080
        self.camera.frame_width = 16
        self.camera.frame_height = 9
        self.camera.background_color = WHITE
        config.frame_rate = 30

        # --- Title ---
        title = Text("Electrostatic Force", font_size=60, color=BLACK).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # --- Helper function to create a charge object ---
        # A charge is represented by a colored circle with a label (+Q or -Q)
        def create_charge(position, charge_sign_str, color):
            charge_circle = Circle(radius=0.5, color=color, fill_opacity=0.8).move_to(position)
            # Label color is white for contrast on colored circles, black if circle is white
            charge_label = MathTex(charge_sign_str, color=WHITE if color != WHITE else BLACK).move_to(charge_circle.get_center())
            return VGroup(charge_circle, charge_label)

        # --- Initial Positions for Charges ---
        initial_pos1 = LEFT * 3.5
        initial_pos2 = RIGHT * 3.5

        # --- Phase 1: Repulsion (Like Charges) ---
        repulsion_text = Text("Like Charges Repel", font_size=40, color=BLACK).next_to(title, DOWN, buff=0.5)

        # Create two positive charges (both RED)
        charge1_pos = create_charge(initial_pos1, "+Q", RED)
        charge2_pos = create_charge(initial_pos2, "+Q", RED)

        self.play(FadeIn(charge1_pos), FadeIn(charge2_pos))
        self.wait(1)

        # Calculate vectors for force arrows to point away from each other
        vec_1_to_2 = (charge2_pos.get_center() - charge1_pos.get_center()).normalize()
        vec_2_to_1 = (charge1_pos.get_center() - charge2_pos.get_center()).normalize()

        # Create force arrows for repulsion
        # Arrow from charge1_pos pointing away from charge2_pos
        arrow1_repel = Arrow(
            start=charge1_pos.get_center() - vec_2_to_1 * 0.5, # Start at edge of charge1
            end=charge1_pos.get_center() - vec_2_to_1 * 2,    # Point further away
            color=ORANGE, stroke_width=5, tip_length=0.3
        )
        # Arrow from charge2_pos pointing away from charge1_pos
        arrow2_repel = Arrow(
            start=charge2_pos.get_center() - vec_1_to_2 * 0.5, # Start at edge of charge2
            end=charge2_pos.get_center() - vec_1_to_2 * 2,    # Point further away
            color=ORANGE, stroke_width=5, tip_length=0.3
        )

        self.play(GrowArrow(arrow1_repel), GrowArrow(arrow2_repel))
        self.wait(0.5)

        self.play(Write(repulsion_text))
        self.wait(1)

        # Animate charges moving apart due to repulsion
        self.play(
            charge1_pos.animate.shift(LEFT * 1.5),
            charge2_pos.animate.shift(RIGHT * 1.5),
            FadeOut(arrow1_repel),
            FadeOut(arrow2_repel),
            run_time=2
        )
        self.wait(1)

        self.play(FadeOut(charge1_pos), FadeOut(charge2_pos), FadeOut(repulsion_text))
        self.wait(1)

        # --- Phase 2: Attraction (Unlike Charges) ---
        attraction_text = Text("Unlike Charges Attract", font_size=40, color=BLACK).next_to(title, DOWN, buff=0.5)

        # Create a positive (RED) and a negative (BLUE) charge
        charge1_pos_attract = create_charge(initial_pos1, "+Q", RED)
        charge2_neg_attract = create_charge(initial_pos2, "-Q", BLUE)

        self.play(FadeIn(charge1_pos_attract), FadeIn(charge2_neg_attract))
        self.wait(1)

        # Recalculate vectors for force arrows to point towards each other
        vec_1_to_2_attract = (charge2_neg_attract.get_center() - charge1_pos_attract.get_center()).normalize()
        vec_2_to_1_attract = (charge1_pos_attract.get_center() - charge2_neg_attract.get_center()).normalize()
        
        # Create force arrows for attraction
        # Arrow from charge1_pos_attract pointing towards charge2_neg_attract
        arrow1_attract = Arrow(
            start=charge1_pos_attract.get_center() + vec_1_to_2_attract * 0.5, # Start at edge of charge1
            end=charge2_neg_attract.get_center() - vec_1_to_2_attract * 0.5, # End at edge of charge2
            color=ORANGE, stroke_width=5, tip_length=0.3
        )
        # Arrow from charge2_neg_attract pointing towards charge1_pos_attract
        arrow2_attract = Arrow(
            start=charge2_neg_attract.get_center() + vec_2_to_1_attract * 0.5, # Start at edge of charge2
            end=charge1_pos_attract.get_center() - vec_2_to_1_attract * 0.5, # End at edge of charge1
            color=ORANGE, stroke_width=5, tip_length=0.3
        )
        
        self.play(GrowArrow(arrow1_attract), GrowArrow(arrow2_attract))
        self.wait(0.5)

        self.play(Write(attraction_text))
        self.wait(1)

        # Animate charges moving together due to attraction
        self.play(
            charge1_pos_attract.animate.shift(RIGHT * 1.5),
            charge2_neg_attract.animate.shift(LEFT * 1.5),
            FadeOut(arrow1_attract),
            FadeOut(arrow2_attract),
            run_time=2
        )
        self.wait(1)

        self.play(FadeOut(charge1_pos_attract), FadeOut(charge2_neg_attract), FadeOut(attraction_text))
        self.wait(1)

        # --- Phase 3: Coulomb's Law (Formula) ---
        coulomb_law_formula = MathTex(
            r"F = k \frac{|q_1 q_2|}{r^2}",
            font_size=60,
            color=BLACK
        ).move_to(ORIGIN)

        # Explanation for the terms in Coulomb's Law
        coulomb_law_explanation = VGroup(
            Text("F: Electrostatic Force", font_size=30, color=BLACK),
            Text("k: Coulomb's Constant", font_size=30, color=BLACK),
            Text("q1, q2: Magnitudes of Charges", font_size=30, color=BLACK),
            Text("r: Distance between Charges", font_size=30, color=BLACK)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(coulomb_law_formula, DOWN, buff=0.8)

        self.play(Write(coulomb_law_formula))
        self.wait(1)
        self.play(FadeIn(coulomb_law_explanation))
        self.wait(3)

        self.play(FadeOut(coulomb_law_formula), FadeOut(coulomb_law_explanation))
        self.wait(1)
        
        self.play(FadeOut(title))
        self.wait(1)