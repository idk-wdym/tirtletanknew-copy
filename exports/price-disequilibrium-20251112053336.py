from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # --- Configuration ---
        self.camera.background_color = WHITE
        config.frame_width = 16  # 1920x1080 aspect ratio (16:9)
        config.frame_height = 9
        config.frame_rate = 30

        # --- 1. Setup Axes and Labels ---
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 12, 1],
            x_length=7,
            y_length=6,
            axis_config={"color": BLACK, "include_numbers": True},
            tips=False
        ).to_edge(DOWN + LEFT, buff=1.0)

        x_label = axes.get_x_axis().get_axis_label(
            Text("Quantity (Q)", font_size=24, color=BLACK), edge=DOWN, direction=RIGHT
        )
        y_label = axes.get_y_axis().get_axis_label(
            Text("Price (P)", font_size=24, color=BLACK), edge=LEFT, direction=UP
        )

        self.play(
            Create(axes),
            FadeIn(x_label, y_label),
            run_time=1.5
        )
        self.wait(0.5)

        # --- 2. Define Supply and Demand Functions ---
        # Demand: P = 10 - Q
        demand_func = lambda q: 10 - q
        demand_graph = axes.plot(demand_func, x_range=[0, 10], color=BLUE)
        demand_label = Text("Demand (D)", font_size=24, color=BLUE).next_to(demand_graph, UP + RIGHT, buff=0.1)

        # Supply: P = 2 + Q
        supply_func = lambda q: 2 + q
        supply_graph = axes.plot(supply_func, x_range=[0, 8], color=RED) # Limit x_range for better visual
        supply_label = Text("Supply (S)", font_size=24, color=RED).next_to(supply_graph, UP + LEFT, buff=0.1)

        self.play(
            Create(demand_graph),
            FadeIn(demand_label),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Create(supply_graph),
            FadeIn(supply_label),
            run_time=1.5
        )
        self.wait(1)

        # --- 3. Find and Highlight Equilibrium ---
        # Equilibrium: 10 - Q = 2 + Q => 8 = 2Q => Q = 4
        # P = 10 - 4 = 6
        equilibrium_q = 4
        equilibrium_p = 6
        equilibrium_point = axes.coords_to_point(equilibrium_q, equilibrium_p)
        eq_dot = Dot(equilibrium_point, color=GREEN, radius=0.1)

        eq_q_line = DashedLine(
            axes.coords_to_point(equilibrium_q, 0),
            equilibrium_point,
            color=GRAY
        )
        eq_p_line = DashedLine(
            axes.coords_to_point(0, equilibrium_p),
            equilibrium_point,
            color=GRAY
        )

        eq_q_label = Text(f"Q*", font_size=24, color=BLACK).next_to(eq_q_line, DOWN, buff=0.1)
        eq_p_label = Text(f"P*", font_size=24, color=BLACK).next_to(eq_p_line, LEFT, buff=0.1)

        equilibrium_text = Text("Equilibrium", font_size=36, color=BLACK).to_edge(UP, buff=0.5)

        self.play(
            FadeIn(equilibrium_text),
            Create(eq_q_line),
            Create(eq_p_line),
            FadeIn(eq_q_label, eq_p_label),
            Create(eq_dot),
            run_time=2
        )
        self.wait(2)
        self.play(FadeOut(equilibrium_text))

        # --- 4. Disequilibrium - Surplus ---
        surplus_price = 8 # Price above equilibrium
        price_line_surplus = axes.get_horizontal_line(
            axes.coords_to_point(0, surplus_price),
            color=PURPLE,
            stroke_width=3
        )
        price_label_surplus = Text(f"P_high", font_size=24, color=PURPLE).next_to(price_line_surplus, LEFT, buff=0.1)

        # Quantity demanded at P_high: 8 = 10 - Q => Q = 2
        qd_surplus = 10 - surplus_price
        qd_point_surplus = axes.coords_to_point(qd_surplus, surplus_price)
        qd_dot_surplus = Dot(qd_point_surplus, color=BLUE, radius=0.08)

        # Quantity supplied at P_high: 8 = 2 + Q => Q = 6
        qs_surplus = surplus_price - 2
        qs_point_surplus = axes.coords_to_point(qs_surplus, surplus_price)
        qs_dot_surplus = Dot(qs_point_surplus, color=RED, radius=0.08)

        # Surplus region
        surplus_region = Polygon(
            qd_point_surplus,
            qs_point_surplus,
            axes.coords_to_point(qs_surplus, equilibrium_p), # Not strictly needed for visual, but for clarity
            axes.coords_to_point(qd_surplus, equilibrium_p), # Not strictly needed for visual, but for clarity
            color=YELLOW,
            fill_opacity=0.4,
            stroke_width=0
        )
        surplus_text = Text("Surplus (Excess Supply)", font_size=36, color=BLACK).to_edge(UP, buff=0.5)

        self.play(
            Transform(eq_p_line, price_line_surplus),
            Transform(eq_p_label, price_label_surplus),
            FadeOut(eq_q_line, eq_q_label, eq_dot),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Create(qd_dot_surplus),
            Create(qs_dot_surplus),
            run_time=1
        )
        self.play(
            FadeIn(surplus_region),
            FadeIn(surplus_text),
            run_time=1.5
        )
        self.wait(2)
        self.play(
            FadeOut(surplus_region, qd_dot_surplus, qs_dot_surplus, surplus_text),
            run_time=1
        )

        # --- 5. Disequilibrium - Shortage ---
        shortage_price = 4 # Price below equilibrium
        price_line_shortage = axes.get_horizontal_line(
            axes.coords_to_point(0, shortage_price),
            color=ORANGE,
            stroke_width=3
        )
        price_label_shortage = Text(f"P_low", font_size=24, color=ORANGE).next_to(price_line_shortage, LEFT, buff=0.1)

        # Quantity demanded at P_low: 4 = 10 - Q => Q = 6
        qd_shortage = 10 - shortage_price
        qd_point_shortage = axes.coords_to_point(qd_shortage, shortage_price)
        qd_dot_shortage = Dot(qd_point_shortage, color=BLUE, radius=0.08)

        # Quantity supplied at P_low: 4 = 2 + Q => Q = 2
        qs_shortage = shortage_price - 2
        qs_point_shortage = axes.coords_to_point(qs_shortage, shortage_price)
        qs_dot_shortage = Dot(qs_point_shortage, color=RED, radius=0.08)

        # Shortage region
        shortage_region = Polygon(
            qs_point_shortage,
            qd_point_shortage,
            axes.coords_to_point(qd_shortage, equilibrium_p), # Not strictly needed for visual, but for clarity
            axes.coords_to_point(qs_shortage, equilibrium_p), # Not strictly needed for visual, but for clarity
            color=PINK,
            fill_opacity=0.4,
            stroke_width=0
        )
        shortage_text = Text("Shortage (Excess Demand)", font_size=36, color=BLACK).to_edge(UP, buff=0.5)

        self.play(
            Transform(eq_p_line, price_line_shortage),
            Transform(eq_p_label, price_label_shortage),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Create(qd_dot_shortage),
            Create(qs_dot_shortage),
            run_time=1
        )
        self.play(
            FadeIn(shortage_region),
            FadeIn(shortage_text),
            run_time=1.5
        )
        self.wait(2)
        self.play(
            FadeOut(shortage_region, qd_dot_shortage, qs_dot_shortage, shortage_text),
            run_time=1
        )

        # --- 6. Return to Equilibrium ---
        # Re-create original equilibrium mobjects for a clean transform back
        final_eq_q_line = DashedLine(
            axes.coords_to_point(equilibrium_q, 0),
            equilibrium_point,
            color=GRAY
        )
        final_eq_p_line = DashedLine(
            axes.coords_to_point(0, equilibrium_p),
            equilibrium_point,
            color=GRAY
        )
        final_eq_q_label = Text(f"Q*", font_size=24, color=BLACK).next_to(final_eq_q_line, DOWN, buff=0.1)
        final_eq_p_label = Text(f"P*", font_size=24, color=BLACK).next_to(final_eq_p_line, LEFT, buff=0.1)
        final_eq_dot = Dot(equilibrium_point, color=GREEN, radius=0.1)

        self.play(
            Transform(eq_p_line, final_eq_p_line),
            Transform(eq_p_label, final_eq_p_label),
            Create(final_eq_q_line),
            Create(final_eq_q_label),
            Create(final_eq_dot),
            run_time=2
        )
        self.wait(2)

        # Final fade out
        self.play(
            FadeOut(axes, x_label, y_label, demand_graph, demand_label,
                    supply_graph, supply_label, eq_p_line, eq_p_label,
                    final_eq_q_line, final_eq_q_label, final_eq_dot),
            run_time=2
        )
        self.wait(1)