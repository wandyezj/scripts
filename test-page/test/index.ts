import { startServer } from "./startServer";
import {serverPort} from "./constants";

// test out the server with 'npm run start'

const port = serverPort;
startServer(port);
console.log(`listening on:\n http://localhost:${port}`);