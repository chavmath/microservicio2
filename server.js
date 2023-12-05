const express = require('express');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3002;

app.use(express.json());

app.get('/verificarLicencia/:cedula', async (req, res) => {
  try {
    const { cedula } = req.params;
    const response = await axios.get(`https://consultaweb.ant.gob.ec/PortalWEB/paginas/clientes/clp_grid_citaciones.jsp?ps_tipo_identificacion=CED&ps_identificacion=${cedula}&ps_placa=`);
    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error en la verificación de la Licencia' });
  }
});

app.listen(PORT, () => {
  console.log(`Servidor de MicroservicioLicencia en http://localhost:${PORT}`);
});
