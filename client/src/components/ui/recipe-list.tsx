import React, { useEffect, useState } from "react";
import { API_BASE_URL } from "@/constants";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";

const RecipeList = () => {
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/recipes`);
        if (response.ok) {
          let data = await response.json();
          // Sort data by name
          data = data.sort((a, b) => a.name.localeCompare(b.name));
          setRecipes(data);
          setLoading(false);
        } else {
          console.error("Failed to fetch recipes");
        }
      } catch (error) {
        console.error("Error fetching recipes:", error);
      }
    };

    fetchRecipes();
  }, []);

  if (loading) return <p>Loading...</p>;

  return (
    <div className="h-1/2 overflow-y-auto mt-10 mb-20">
      Available Recipes
      <Grid container spacing={2} className="py-10">
        {recipes.map((recipe) => (
          <Grid key={recipe.id} item xs={12} sm={6} md={4} lg={4}>
            <Card>
              <CardContent>
                <Typography variant="body1" component="div">
                  {recipe.name}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

export default RecipeList;
