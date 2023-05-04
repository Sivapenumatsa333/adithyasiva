// This scripts take all files from the source folder and
// copy them to S3 bucket

import { S3, PutObjectCommand } from "@aws-sdk/client-s3";
import { Upload } from '@aws-sdk/lib-storage';
import fs from "fs";
import path from "path";
//const fs = require('fs');
// const path = require('path');


// set credentials and region
// const AWS_ACCESS_KEY_ID = process.env.AWS_ACCESS_KEY_ID;
// const AWS_SECRET_ACCESS_KEY = process.env.AWS_SECRET_ACCESS_KEY;
// const AWS_DEFAULT_REGION = process.env.AWS_DEFAULT_REGION;
// AWS.config.update({
//   accessKeyId: AWS_ACCESS_KEY_ID,
//   secretAccessKey: AWS_SECRET_ACCESS_KEY,
//   region: AWS_DEFAULT_REGION,
// });

const s3 = new S3();

// const BUCKET_NAME = 'adithyasiva.shop';
const BUCKET_NAME = 'prueba.test.sh';
const SOURCE_FOLDER = 'source';


export const handler = async(event) => {
    const files = fs.readdirSync(SOURCE_FOLDER);
    
    for (const file of files) {
      const filePath = path.join(SOURCE_FOLDER, file);
      const fileContent = fs.readFileSync(filePath);

      const params = {
        Bucket: BUCKET_NAME,
        Key: file,
        Body: fileContent,
      };
      const command = new PutObjectCommand(params);
      await s3.send(command);
    }

    const response = {
        statusCode: 200,
        body: JSON.stringify('Copied!!'),
    };
    return response;
};
