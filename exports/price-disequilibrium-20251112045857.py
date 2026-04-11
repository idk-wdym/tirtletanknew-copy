from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # --- Configuration ---
        # Set resolution to 1920x1080 and 30 FPS
        self.camera.background_color = WHITE
        config.pixel_width = 1920
        config.pixel_height = 1080
        config.frame_rate = 30

        # --- 1. Setup Axes and Curves ---
        # Define the axes for Quantity (Q) and Price (P)
        x_range = [0, 12, 2] # Quantity range
        y_range = [0, 12, 2] # Price range
        self.axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=8,
            y_length=6,
            axis_config={"color": BLACK, "include_numbers": True},
            tips=False # Do not include arrow tips on axes
        ).to_edge(DOWN + LEFT, buff=1.0) # Position the graph on the bottom-left

        # Labels for axes
        x_label = self.axes.get_x_axis_label("Quantity (Q)").next_to(self.axes.x_axis, DOWN, buff=0.2).set_color(BLACK)
        y_label = self.axes.get_y_axis_label("Price (P)").next_to(self.axes.y_axis, LEFT, buff=0.2).set_color(BLACK)

        # Define Demand and Supply functions
        # Demand: P = 8 - 0.5Q (Downward sloping)
        demand_func = lambda x: 8 - 0.5 * x
        # Supply: P = 0.5Q + 2 (Upward sloping)
        supply_func = lambda x: 0.5 * x + 2

        # Create the graph objects for demand and supply curves
        demand_curve = self.axes.get_graph(demand_func, x_range=[0, 12], color=BLUE)
        supply_curve = self.axes.get_graph(supply_func, x_range=[0, 12], color=RED)

        # Labels for the curves
        demand_label = Text("Demand", font_size=28, color=BLUE).next_to(demand_curve, UP + RIGHT, buff=0.1)
        supply_label = Text("Supply", font_size=28, color=RED).next_to(supply_curve, UP + LEFT, buff=0.1)

        # Group all initial graph elements for easier manipulation
        graph_elements = VGroup(self.axes, x_label, y_label, demand_curve, supply_curve, demand_label, supply_label)

        # Animation: Draw axes and labels
        self.play(
            Create(self.axes),
            Write(x_label),
            Write(y_label),
            run_time=2
        )
        # Animation: Draw demand curve and label
        self.play(
            Create(demand_curve),
            Write(demand_label),
            run_time=1.5
        )
        # Animation: Draw supply curve and label
        self.play(
            Create(supply_curve),
            Write(supply_label),
            run_time=1.5
        )
        self.wait(1)

        # --- 2. Equilibrium Point ---
        # Calculate equilibrium point (Q_e, P_e) where demand_func = supply_func
        # 8 - 0.5Q = 0.5Q + 2  =>  6 = Q  => Q_e = 6
        # P_e = 0.5 * 6 + 2 = 5
        equilibrium_q = 6
        equilibrium_p = 5
        equilibrium_point_coords = self.axes.coords_to_point(equilibrium_q, equilibrium_p)
        eq_dot = Dot(equilibrium_point_coords, color=GREEN, radius=0.1)

        # Dashed lines projecting equilibrium point to axes
        eq_q_line = self.axes.get_vertical_line(equilibrium_point_coords, line_config={"dashed_ratio": 0.8, "color": GREEN})
        eq_p_line = self.axes.get_horizontal_line(equilibrium_point_coords, line_config={"dashed_ratio": 0.8, "color": GREEN})

        # Labels for equilibrium price and quantity
        eq_q_label = MathTex("Q_e", font_size=32, color=GREEN).next_to(eq_q_line, DOWN, buff=0.1)
        eq_p_label = MathTex("P_e", font_size=32, color=GREEN).next_to(eq_p_line, LEFT, buff=0.1)

        equilibrium_text = Text("Market Equilibrium", font_size=40, color=BLACK).to_edge(UP, buff=0.5)

        # Animation: Show equilibrium point and projections
        self.play(
            Create(eq_dot),
            Create(eq_q_line),
            Create(eq_p_line),
            Write(eq_q_label),
            Write(eq_p_label),
            run_time=2
        )
        self.play(Write(equilibrium_text))
        self.wait(2)

        # Group equilibrium elements for easy fading later
        equilibrium_group = VGroup(eq_dot, eq_q_line, eq_p_line, eq_q_label, eq_p_label, equilibrium_text)

        # --- 3. Surplus (Price above equilibrium) ---
        self.play(FadeOut(equilibrium_group)) # Fade out equilibrium elements to focus on disequilibrium
        self.wait(0.5)

        surplus_price = 7 # Set a price above equilibrium (P_s > P_e)
        surplus_price_line = self.axes.get_horizontal_line(self.axes.coords_to_point(0, surplus_price), line_config={"color": PURPLE, "stroke_width": 3})
        surplus_p_label = MathTex("P_s", font_size=32, color=PURPLE).next_to(surplus_price_line, LEFT, buff=0.1)

        # Calculate quantities demanded and supplied at surplus_price
        # Q_d = (8 - P_s) / 0.5
        q_demanded_surplus = (8 - surplus_price) / 0.5
        # Q_s = (P_s - 2) / 0.5
        q_supplied_surplus = (surplus_price - 2) / 0.5

        # Points on curves at surplus_price
        demand_point_surplus = self.axes.coords_to_point(q_demanded_surplus, surplus_price)
        supply_point_surplus = self.axes.coords_to_point(q_supplied_surplus, surplus_price)

        # Projections to x-axis for Q_d and Q_s
        q_demanded_surplus_line = self.axes.get_vertical_line(demand_point_surplus, line_config={"dashed_ratio": 0.8, "color": BLUE})
        q_supplied_surplus_line = self.axes.get_vertical_line(supply_point_surplus, line_config={"dashed_ratio": 0.8, "color": RED})

        # Labels for Q_d and Q_s at surplus price
        q_demanded_surplus_label = MathTex("Q_d", font_size=32, color=BLUE).next_to(q_demanded_surplus_line, DOWN, buff=0.1)
        q_supplied_surplus_label = MathTex("Q_s", font_size=32, color=RED).next_to(q_supplied_surplus_line, DOWN, buff=0.1)

        surplus_text = Text("Surplus (Excess Supply)", font_size=40, color=BLACK).to_edge(UP, buff=0.5)
        # Highlight the segment on the price line representing the surplus (Q_s - Q_d)
        surplus_segment = Line(demand_point_surplus, supply_point_surplus, color=YELLOW, stroke_width=8)

        # Animation: Show surplus scenario
        self.play(
            Create(surplus_price_line),
            Write(surplus_p_label),
            run_time=1
        )
        self.play(
            Create(q_demanded_surplus_line),
            Write(q_demanded_surplus_label),
            Create(q_supplied_surplus_line),
            Write(q_supplied_surplus_label),
            run_time=2
        )
        self.play(
            Create(surplus_segment), # Highlight the surplus quantity
            Write(surplus_text)
        )
        self.wait(2)

        # Animation: Price adjustment - price moves down towards equilibrium
        # Create copies of the price line and label to animate their movement
        anim_price_line = surplus_price_line.copy()
        anim_p_label = surplus_p_label.copy()

        self.play(
            anim_price_line.animate.move_to(self.axes.coords_to_point(0, equilibrium_p), aligned_edge=LEFT), # Move price line to equilibrium price
            anim_p_label.animate.next_to(self.axes.coords_to_point(0, equilibrium_p), LEFT, buff=0.1).set_color(GREEN).set_text("P_e"), # Change label to P_e
            FadeOut(surplus_segment, q_demanded_surplus_line, q_supplied_surplus_line, q_demanded_surplus_label, q_supplied_surplus_label, surplus_text),
            run_time=3
        )
        self.play(FadeOut(anim_price_line, anim_p_label)) # Fade out the animated elements
        self.wait(0.5)

        # --- 4. Shortage (Price below equilibrium) ---
        shortage_price = 3 # Set a price below equilibrium (P_d < P_e)
        shortage_price_line = self.axes.get_horizontal_line(self.axes.coords_to_point(0, shortage_price), line_config={"color": ORANGE, "stroke_width": 3})
        shortage_p_label = MathTex("P_d", font_size=32, color=ORANGE).next_to(shortage_price_line, LEFT, buff=0.1)

        # Calculate quantities demanded and supplied at shortage_price
        # Q_d = (8 - P_d) / 0.5
        q_demanded_shortage = (8 - shortage_price) / 0.5
        # Q_s = (P_d - 2) / 0.5
        q_supplied_shortage = (shortage_price - 2) / 0.5

        # Points on curves at shortage_price
        demand_point_shortage = self.axes.coords_to_point(q_demanded_shortage, shortage_price)
        supply_point_shortage = self.axes.coords_to_point(q_supplied_shortage, shortage_price)

        # Projections to x-axis for Q_d and Q_s
        q_demanded_shortage_line = self.axes.get_vertical_line(demand_point_shortage, line_config={"dashed_ratio": 0.8, "color": BLUE})
        q_supplied_shortage_line = self.axes.get_vertical_line(supply_point_shortage, line_config={"dashed_ratio": 0.8, "color": RED})

        # Labels for Q_d and Q_s at shortage price
        q_demanded_shortage_label = MathTex("Q_d", font_size=32, color=BLUE).next_to(q_demanded_shortage_line, DOWN, buff=0.1)
        q_supplied_shortage_label = MathTex("Q_s", font_size=32, color=RED).next_to(q_supplied_shortage_line, DOWN, buff=0.1)

        shortage_text = Text("Shortage (Excess Demand)", font_size=40, color=BLACK).to_edge(UP, buff=0.5)
        # Highlight the segment on the price line representing the shortage (Q_d - Q_s)
        shortage_segment = Line(supply_point_shortage, demand_point_shortage, color=PINK, stroke_width=8)

        # Animation: Show shortage scenario
        self.play(
            Create(shortage_price_line),
            Write(shortage_p_label),
            run_time=1
        )
        self.play(
            Create(q_demanded_shortage_line),
            Write(q_demanded_shortage_label),
            Create(q_supplied_shortage_line),
            Write(q_supplied_shortage_label),
            run_time=2
        )
        self.play(
            Create(shortage_segment), # Highlight the shortage quantity
            Write(shortage_text)
        )
        self.wait(2)

        # Animation: Price adjustment - price moves up towards equilibrium
        anim_price_line = shortage_price_line.copy()
        anim_p_label = shortage_p_label.copy()

        self.play(
            anim_price_line.animate.move_to(self.axes.coords_to_point(0, equilibrium_p), aligned_edge=LEFT), # Move price line to equilibrium price
            anim_p_label.animate.next_to(self.axes.coords_to_point(0, equilibrium_p), LEFT, buff=0.1).set_color(GREEN).set_text("P_e"), # Change label to P_e
            FadeOut(shortage_segment, q_demanded_shortage_line, q_supplied_shortage_line, q_demanded_shortage_label, q_supplied_shortage_label, shortage_text),
            run_time=3
        )
        self.play(FadeOut(anim_price_line, anim_p_label)) # Fade out the animated elements
        self.wait(0.5)

        # --- 5. Return to Equilibrium ---
        equilibrium_text_restored = Text("Market Equilibrium Restored", font_size=40, color=BLACK).to_edge(UP, buff=0.5)
        self.play(
            FadeIn(equilibrium_group), # Re-introduce the original equilibrium elements
            Write(equilibrium_text_restored)
        )
        self.wait(3)
        self.play(FadeOut(graph_elements, equilibrium_group, equilibrium_text_restored))
        self.wait(1)